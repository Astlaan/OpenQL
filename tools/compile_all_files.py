import glob
import os
import importlib
import argparse
from openql import openql as ql
import sys
from io import StringIO
from joblib import Parallel, delayed, cpu_count

#very confusing function!
def generate_new_dest_dir(input, mapper):
	folders = [name for name in os.listdir(input) if os.path.isdir(os.path.join(input,name)) and ("mapper="+mapper+"_" in name)]
	if folders:
		new_number = max([int(folder.split("mapper="+mapper+"_")[1]) for folder in folders])+1
	else:
		new_number = 1
	return "mapper=" + mapper + "_" + str(new_number)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Validate OpenQL compiler')
	parser.add_argument('-m', type=str, help='mapper')
	parser.add_argument('--one', type=str, help='maxfidelity_1qbgatefid')
	parser.add_argument('--two', type=str, help='maxfidelity_2qbgatefid')
	parser.add_argument('--idle', type=str, help='maxfidelity_idlefid')
	parser.add_argument('--output', type=str, help='maxfidelity_outputmode')
	parser.add_argument('--dir', type=str, help='output directory')
	parser.add_argument('--single', action="store_true", default=False, help='Single cpu compilation')
	parser.add_argument('--debug', action="store_true", default=False, help='Output metrics.h debug code')
	parser.add_argument('--indir', type=str, help='Input directory')

	args = parser.parse_args()

	if args.indir:
		indir = os.path.join("./test_files", args.indir)
	else:
		indir = "test_files/"
	# indir = './test_files/'
	# if not args.outdir:
		# outdir = os.path.join(indir, "/output")

	curdir = os.getcwd()
	# os.chdir(os.path.join(curdir, indir))
	files = glob.glob(indir + '/*.py')
	files = list(map(os.path.basename, files))
	files = list(map(lambda x: x.replace('.py', ''), files))
	# os.chdir(curdir)
	# print(indir + '*.py')
	
	sys.path.append(os.path.join(curdir, indir))
	print("INDIR = ", indir)

	if __file__ in files:
		files.remove(__file__)

	ql.set_option('quantumsim', 'qsoverlay')
	ql.set_option('write_report_files', 'yes')
	ql.set_option('write_qasm_files', 'yes')
	print(files)


#VARIOUS OPTIONS

	#Measurement
	measurement = False

	#Some compiler options
	mapper=args.m
	log_level = 'LOG_NOTHING'
	scheduler = 'ALAP' #= ALAP
	optimize = 'no' #= no
	scheduler_uniform = 'no' #= no
	initialplace = 'no' #= no
	scheduler_post179 = 'yes' #= yes
	scheduler_commute = 'yes' #= yes
	mapusemoves = 'no'  #= yes 
	maptiebreak = 'random' #= random

	# output_dir_name = 'test_output/mapper=' + mapper

	#add other options here (overring the options above will not work! change the value in the options above instead!)
	# mapper = 'maxfidelity' #= minextendrc

	def set_options(): 
		# ql.set_option("maxfidelity_1qbgatefid", "0.999")
		# ql.set_option("maxfidelity_2qbgatefid", "0.99")
		# ql.set_option("maxfidelity_idlefid", "0.999334")
		# ql.set_option("maxfidelity_outputmode", "average")
		if args.debug:
			ql.set_option("maxfidelity_loglevel", "debug")
		
		ql.set_option("maxfidelity_1qbgatefid", args.one)
		ql.set_option("maxfidelity_2qbgatefid", args.two)
		ql.set_option("maxfidelity_idlefid", args.idle)
		ql.set_option("maxfidelity_outputmode", args.output)

		ql.set_option('decompose_toffoli', "no") # = "no";
		ql.set_option("prescheduler", "yes") # = "yes";
		ql.set_option("cz_mode", "manual") # = "manual";
		ql.set_option("clifford_premapper", "no") # = "yes";
		ql.set_option("clifford_postmapper", "no") # = "yes";
		ql.set_option("mapinitone2one", "yes") # = "yes";
		ql.set_option("mapassumezeroinitstate", "no") # = "no";
		ql.set_option("initialplace2qhorizon", "0") # = "0";
		ql.set_option("maplookahead", "noroutingfirst") # = "noroutingfirst";
		ql.set_option("mappathselect", "all") # = "all";
		ql.set_option("maprecNN2q", "no") # = "no";
		ql.set_option("mapselectmaxlevel", "0") # = "0";
		ql.set_option("mapselectmaxwidth", "min") # = "min";
		ql.set_option("mapselectswaps", "all") # = "all";
		ql.set_option("mapreverseswap", "yes") # = "yes";
		ql.set_option('quantumsim', 'qsoverlay') # = "no";
		ql.set_option('write_report_files', 'yes') # = "no";
		ql.set_option('write_qasm_files', 'yes') # = "no";


	#==== Create output folder
	all_results_dir = "test_output"
	curdir = os.getcwd()
	output_dir_name = os.path.join(indir, all_results_dir)
	# if args.dir:
	# 	all_results_dir = os.path.join(all_results_dir, args.dir)
	# 	if not os.path.exists(os.path.join(indir, all_results_dir)):
	# 		os.makedirs(os.path.join(indir, all_results_dir))
	# result_dir = generate_new_dest_dir(os.path.join(indir, all_results_dir), mapper)
	# output_dir_name = os.path.join(all_results_dir, result_dir)
	if not os.path.exists(output_dir_name):
		os.makedirs(output_dir_name)
	print("OUTDIR = ", output_dir_name)
	# print(os.path.join(indir, output_dir_name))

	#=== Serial Compilation
	# for file in files:
	# 	imported = importlib.import_module(os.path.join(file.replace(".py", "")))
	# 	try:
	# 		imported.circuit('test_mapper17.json', scheduler = scheduler, sched_commute = scheduler_commute, mapper = mapper, uniform_sched = scheduler_uniform, new_scheduler = scheduler_post179,  moves = mapusemoves, maptiebreak = maptiebreak, measurement = measurement, optimize = optimize, initial_placement = initialplace, output_dir_name = output_dir_name, log_level = log_level)
	# 	except Exception as e:
	# 		print(str(e))

	# === Parallel Compilation (does not work! Somehow, the ql.set_options don't take effect within each of the worker processes)
	# def parallel_import_compile(file, scheduler, mapper, scheduler_uniform, scheduler_post179, mapusemoves, maptiebreak, measurement, optimize, output_dir_name, log_level):
	# 	imported = importlib.import_module(os.path.join(file.replace(".py", "")))
	# 	try:
	# 		imported.circuit('test_mapper17.json', )
	# 	except Exception as e:
	# 		print(str(e))

	def parallel_import_compile_v2(files, scheduler , mapper , scheduler_commute, scheduler_uniform , scheduler_post179 ,  mapusemoves , maptiebreak , measurement , optimize , initialplace , output_dir_name , log_level ):
		print("Import started")
		imported_list = [importlib.import_module(os.path.join(file.replace(".py", ""))) for file in files]
		print("Import complete")
		def _parallel_import_compile_v2(imported, scheduler , mapper , scheduler_commute, scheduler_uniform , scheduler_post179 ,  mapusemoves , maptiebreak , measurement , optimize , initialplace , output_dir_name , log_level ):
			#Set correct options in subprocess
			set_options()
			#print(ql.get_option('maxfidelity_1qbgatefid'))
			#print(ql.get_option('maxfidelity_2qbgatefid'))
			#print(ql.get_option('maxfidelity_idlefid'))
			#print(ql.get_option('maxfidelity_outputmode'))

			try:
				imported.circuit("/home/dmalvalada/bulk/openql_tools/test_files/test_mapper17.json", scheduler = scheduler, sched_commute = scheduler_commute, mapper = mapper, uniform_sched = scheduler_uniform, new_scheduler = scheduler_post179,  moves = mapusemoves, maptiebreak = maptiebreak, measurement = measurement, optimize = optimize, initial_placement = initialplace, output_dir_name = output_dir_name, log_level = log_level)
			except Exception as e:
				print(str(e))
		# def _test():
		# 	set_options()
		# 	parameters = ["unique_output: " + ql.get_option("unique_output") + '\n'  ,
		# 		"optimize: " + ql.get_option("optimize") + '\n'  ,
		# 		"use_default_gates: " + ql.get_option("use_default_gates") + '\n'  ,
		# 		"decompose_toffoli: " + ql.get_option("decompose_toffoli") + '\n'  ,
		# 		"quantumsim: " + ql.get_option("quantumsim") + '\n'  ,
		# 		"prescheduler: " + ql.get_option("prescheduler") + '\n'  ,
		# 		"scheduler: " + ql.get_option("scheduler") + '\n'  ,
		# 		"scheduler_uniform: " + ql.get_option("scheduler_uniform") + '\n'  ,
		# 		"clifford_premapper: " + ql.get_option("clifford_premapper") + '\n'  ,
		# 		"mapper: " +           ql.get_option("mapper") + '\n'  ,
		# 		"mapinitone2one: " +   ql.get_option("mapinitone2one") + '\n'  ,
		# 		"initialplace: " +     ql.get_option("initialplace") + '\n'  ,
		# 		"initialplace2qhorizon: " +ql.get_option("initialplace2qhorizon") + '\n'  ,
		# 		"maplookahead: " +     ql.get_option("maplookahead") + '\n'  ,
		# 		"mappathselect: " +    ql.get_option("mappathselect") + '\n'  ,
		# 		"maptiebreak: " +      ql.get_option("maptiebreak") + '\n'  ,
		# 		"mapusemoves: " +      ql.get_option("mapusemoves") + '\n'  ,
		# 		"mapreverseswap: " +   ql.get_option("mapreverseswap") + '\n'  ,
		# 		"mapselectswaps: " +   ql.get_option("mapselectswaps") + '\n'  ,
		# 		"clifford_postmapper: " + ql.get_option("clifford_postmapper") + '\n'  ,
		# 		"scheduler_post179: " + ql.get_option("scheduler_post179") + '\n'  ,
		# 		"scheduler_commute: " + ql.get_option("scheduler_commute") + '\n'  ,
		# 		"cz_mode: " + ql.get_option("cz_mode") + '\n'  ,
		# 		"mapassumezeroinitstate: " + ql.get_option("mapassumezeroinitstate") + '\n' ,
		# 		"maprecNN2q: " + ql.get_option("maprecNN2q") + '\n' ,
		# 		"mapselectmaxlevel: " + ql.get_option("mapselectmaxlevel") + '\n' ,
		# 		"mapselectmaxwidth: " + ql.get_option("mapselectmaxwidth") + '\n' ,

		# 		"measurement: " + ('yes' if measurement else 'no') + '\n' ,				  

		# 		"maxfidelity_1qbgatefid: " + ql.get_option("maxfidelity_1qbgatefid") + '\n'  , 
		# 		"maxfidelity_2qbgatefid: " + ql.get_option("maxfidelity_2qbgatefid") + '\n'  , 
		# 		"maxfidelity_idlefid: "	 + ql.get_option("maxfidelity_idlefid") + '\n'   ,
		# 		"maxfidelity_outputmode: " + ql.get_option("maxfidelity_outputmode") + '\n'
		# 		'quantumsim' + ql.get_option( 'quantumsim') + '\n',
		# 		'write_report_files' + ql.get_option( 'write_report_files') + '\n',
		# 		'write_qasm_files' + ql.get_option( 'write_qasm_files')	+ '\n']
		# 	print(''.join(parameters))

		if args.single:
			Parallel(n_jobs=1, verbose=8)(delayed(_parallel_import_compile_v2)(imported, scheduler , mapper , scheduler_commute, scheduler_uniform , scheduler_post179 ,  mapusemoves , maptiebreak , measurement , optimize , initialplace , output_dir_name , log_level ) for imported in imported_list)
		else:
			Parallel(n_jobs=cpu_count(), verbose=8)(delayed(_parallel_import_compile_v2)(imported, scheduler , mapper , scheduler_commute, scheduler_uniform , scheduler_post179 ,  mapusemoves , maptiebreak , measurement , optimize , initialplace , output_dir_name , log_level ) for imported in imported_list)
		# Parallel(n_jobs=1, verbose=8)(delayed(_test)() for i in range(1))
		

	parallel_import_compile_v2(files, scheduler , mapper , scheduler_commute, scheduler_uniform , scheduler_post179 ,  mapusemoves , maptiebreak , measurement , optimize , initialplace , output_dir_name , log_level)	

	#==== DO NOT TOUCH HERE (meant to provide some redundancy, so that the parameters variable won't stop working when parallel compilation is fixed):
	#This is because these parameters are only set within each file from qbench
	set_options()
	ql.set_option("log_level", log_level)
	ql.set_option("scheduler", scheduler)
	ql.set_option("mapper", mapper)
	ql.set_option("optimize", optimize)
	ql.set_option("scheduler_uniform", scheduler_uniform)
	ql.set_option("initialplace", initialplace)
	ql.set_option("scheduler_post179", scheduler_post179)
	ql.set_option("scheduler_commute", scheduler_commute)
	ql.set_option("mapusemoves", mapusemoves)
	ql.set_option("maptiebreak", maptiebreak)

	#============== Store the options in a file
	parameters = ["unique_output: " + ql.get_option("unique_output") + '\n'  ,
				  "optimize: " + ql.get_option("optimize") + '\n'  ,
				  "use_default_gates: " + ql.get_option("use_default_gates") + '\n'  ,
				  "decompose_toffoli: " + ql.get_option("decompose_toffoli") + '\n'  ,
				  "quantumsim: " + ql.get_option("quantumsim") + '\n'  ,
				  "prescheduler: " + ql.get_option("prescheduler") + '\n'  ,
				  "scheduler: " + ql.get_option("scheduler") + '\n'  ,
				  "scheduler_uniform: " + ql.get_option("scheduler_uniform") + '\n'  ,
				  "clifford_premapper: " + ql.get_option("clifford_premapper") + '\n'  ,
				  "mapinitone2one: " +   ql.get_option("mapinitone2one") + '\n'  ,
				  "initialplace: " +     ql.get_option("initialplace") + '\n'  ,
				  "initialplace2qhorizon: " +ql.get_option("initialplace2qhorizon") + '\n'  ,
				  "maplookahead: " +     ql.get_option("maplookahead") + '\n'  ,
				  "mappathselect: " +    ql.get_option("mappathselect") + '\n'  ,
				  "maptiebreak: " +      ql.get_option("maptiebreak") + '\n'  ,
				  "mapusemoves: " +      ql.get_option("mapusemoves") + '\n'  ,
				  "mapreverseswap: " +   ql.get_option("mapreverseswap") + '\n'  ,
				  "mapselectswaps: " +   ql.get_option("mapselectswaps") + '\n'  ,
				  "clifford_postmapper: " + ql.get_option("clifford_postmapper") + '\n'  ,
				  "scheduler_post179: " + ql.get_option("scheduler_post179") + '\n'  ,
				  "scheduler_commute: " + ql.get_option("scheduler_commute") + '\n'  ,
				  "cz_mode: " + ql.get_option("cz_mode") + '\n'  ,
				  "mapassumezeroinitstate: " + ql.get_option("mapassumezeroinitstate") + '\n' ,
				  "maprecNN2q: " + ql.get_option("maprecNN2q") + '\n' ,
				  "mapselectmaxlevel: " + ql.get_option("mapselectmaxlevel") + '\n' ,
				  "mapselectmaxwidth: " + ql.get_option("mapselectmaxwidth") + '\n' ,

				  "measurement: " + ('yes' if measurement else 'no') + '\n' ,				  

				  "mapper: " +           ql.get_option("mapper") + '\n'  ,
				  "maxfidelity_1qbgatefid: " + ql.get_option("maxfidelity_1qbgatefid") + '\n'  , 
				  "maxfidelity_2qbgatefid: " + ql.get_option("maxfidelity_2qbgatefid") + '\n'  , 
				  "maxfidelity_idlefid: "	 + ql.get_option("maxfidelity_idlefid") + '\n'   ,
				  "maxfidelity_outputmode: " + ql.get_option("maxfidelity_outputmode") + '\n'
	]
	print("Wrote files to:", output_dir_name)
	print("Writing parameters to:", 'test_files', output_dir_name,'parameters.txt')
	with open(os.path.join(output_dir_name,'parameters.txt'), 'w') as fopen:
		fopen.writelines(parameters)
	# with open(os.path.join('test_files', 'test_output','parameters_all.txt'), 'a') as fopen:
	# 	fopen.writelines(["\n\n\n", "=== " + indir + " ===\n"])
	# 	fopen.writelines(parameters)
