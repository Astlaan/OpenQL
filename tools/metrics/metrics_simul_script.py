import importlib
import sys
import os
import pandas as pd
from tqdm import tqdm
from matplotlib import pyplot as plt
import argparse
from datetime import datetime

#LAPTOP
# sys.path.append('C:\\Users\\Diogo\\Google Drive\\TUDelft\\THESIS\\Code\\MYCODE\\OpenQL\\tools\\metrics')
# os.chdir('C:\\Users\\Diogo\\Google Drive\\TUDelft\\THESIS\\Code\\MYCODE\\OpenQL\\tools\\metrics')
# openql_manager = importlib.import_module('openql_manager')
# importlib.reload(openql_manager)

#SERVER
os.chdir('/home/dmalvalada/bulk/openql_tools/metrics')
import openql_manager



def start(database, folder, allow_gpu):
	print("Procedure started!")
	manager = openql_manager.SimManager(database)
	curdir = os.getcwd()

	input_path = os.path.join(curdir, "../test_files/", folder)
	parameters = openql_manager.import_parameters_from_file(os.path.join(input_path, 'parameters.txt'))
	sys.path.append(os.path.abspath(input_path))
	end_pattern = "quantumsim_mapped.py"
	test_files = openql_manager.get_test_file_names(input_path, end_pattern = end_pattern)
	file_import_dict = {}
	compiled_circ_names = tuple(manager.df["circ_name"])
	for file in test_files:
		circ_name = file.replace('_quantumsim_mapped', '')
		if circ_name in compiled_circ_names:
			continue
		circuit_file = manager.import_circuit_file(file)
		file_import_dict[circ_name] = circuit_file
	
	df_load = []
	noise_flag = True
	noisy_circ_dict = openql_manager.parallel_generate_circuit(file_import_dict, noise_flag, slurm = True)
	print("===Simulation! (noise_flag =", noise_flag, "):")
	for circ_name, circuit in tqdm(noisy_circ_dict.items()):
		measurement = manager.simulate(circuit, allow_gpu = allow_gpu)
		# bundle = {'circ_name': circ_name, 'mapper': parameters['mapper'], 'parameters' : parameters,'sim_noisy': measurement}
		bundle = {'circ_name': circ_name, 'mapper': folder, 'parameters' : parameters,'sim_noisy': measurement}
		df_load.append(bundle)
	# manager.df = manager.df.append(pd.DataFrame(df_load))
	temp_db = pd.DataFrame(df_load)


	noise_flag = False
	clean_circ_dict = openql_manager.parallel_generate_circuit(file_import_dict, noise_flag, slurm = True)
	#print("===Simulation! (noise_flag =", noise_flag, "):")
	for circ_name, circuit in tqdm(clean_circ_dict.items()):
		measurement = manager.simulate(circuit, allow_gpu = allow_gpu)
		# manager.df.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters'] == parameters) , 'sim_clean'] = [measurement]
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters'] == parameters) , 'sim_clean'] = [measurement]


	#=== STATS
	print("Retrieving Stats...")
	test_files_compiler_out = [f.replace(manager.quantumsim_pattern_mapped, manager.compiler_out_report_pattern) for f in test_files]
	file_depth_dict = {}
	file_size_dict = {}
	file_two_qubit_dict = {}
	score1_dict = {}
	score2_dict = {}
	score3_dict = {}
	score4_dict = {}
	for file in test_files_compiler_out:
		file_depth_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_depth(os.path.join(input_path, file))
		file_size_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_size(os.path.join(input_path, file))
		file_two_qubit_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_non_single_qubit_gates(os.path.join(input_path, file))
		score1_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_score(os.path.join(input_path, file), pattern = "Score1")
		score2_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_score(os.path.join(input_path, file), pattern = "Score2")
		score3_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_score(os.path.join(input_path, file), pattern = "Score3")
		score4_dict[file.replace(manager.compiler_out_report_pattern, '')] = manager.get_score(os.path.join(input_path, file), pattern = "Score4")

	for circ_name, size in file_size_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'size'] = size
		# manager.df.loc[lambda df: (df['circ_name'] == circ_name) & (df['mapper']== parameters['mapper']) & (df['parameters']== parameters), 'size'] = size
	for circ_name, depth in file_depth_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'depth'] = depth
		# manager.df.loc[lambda df: (df['circ_name'] == circ_name) & (df['mapper']== parameters['mapper']) & (df['parameters']== parameters), 'depth'] = depth
	for circ_name, two_qubit_gates in file_two_qubit_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'two_qubit'] = two_qubit_gates
		# manager.df.loc[lambda df: (df['circ_name'] == circ_name) & (df['mapper']== parameters['mapper']) & (df['parameters']== parameters), 'two_qubit'] = two_qubit_gates
	for circ_name, score in score1_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'score1'] = score
	for circ_name, score in score2_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'score2'] = score
	for circ_name, score in score3_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'score3'] = score
	for circ_name, score in score4_dict.items():
		temp_db.loc[lambda df: (df['circ_name'] == circ_name) & (df['parameters']== parameters), 'score4'] = score			
		# manager.df.loc[lambda df: (df['circ_name'] == circ_name) & (df['mapper']== parameters['mapper']) & (df['parameters']== parameters), 'two_qubit'] = two_qubit_gates

	print("Retrieving Stats finished!")

	#=== FIDELITY CALCULATION
	print("Calculating Fidelity...")
	temp_db['clean_answer'] = temp_db.apply(lambda row : openql_manager.get_correct_result(row['sim_clean'])[0], axis=1 )
	temp_db['clean_answer_prob'] = temp_db.apply(lambda row : openql_manager.get_correct_result(row['sim_clean'])[1], axis=1 )
	temp_db['fidelity'] = temp_db.apply(lambda row : openql_manager.get_fidelity(row['sim_noisy'], row['clean_answer']) if row['clean_answer'] else openql_manager.get_fidelity(row['sim_noisy'], row['sim_clean']), axis=1 )
	print("Calculating Fidelity finished!...")

	#=== JOIN WITH EXISTING DB
	manager.df = manager.df.append(temp_db)


	#=== To make sure that we don't have duplicated data (based on the 'circ_name' and 'parameters' columns)
	manager.drop_duplicates() #In practice doesn't have an effect now: Duplicates are impossible due to an fatal error with the = [measurement] part when duplicates try to exist

	#=== SAVE
	manager.save()
	#=== Save compact version (no 'sim_noisy' column)
	manager.df.drop(['sim_noisy'], axis=1)
	db_path = manager.db_path
	db_name, extension = os.path.basename(db_path).split('.')
	db_path = os.path.join(os.path.dirname(db_path), db_name + "_compact" + "." + extension)

	#=== Tag folder as compiled
	# os.rename(input_path, input_path + "_c")

if __name__== "__main__":

	parser = argparse.ArgumentParser(description='Check validity of files in a given directory')
	parser.add_argument('--db', type=str)
	parser.add_argument('--folder', type=str)
	parser.add_argument('-c', action="store_true", default=False)
	

	args = parser.parse_args()
	if not args.db or not args.folder:
		print("Please provide both database file and folder name.")
		exit()

	if args.c:
		allow_gpu = False
	else:
		allow_gpu = True

	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

	print("=== Running metrics_simul.", dt_string)
	print(args.db, args.folder)

	start(args.db, args.folder, allow_gpu)
	exit()
	
