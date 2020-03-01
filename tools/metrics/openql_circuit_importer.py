from dataclasses import dataclass

# def laptop():
# 	sys.path.append('C:\\Users\\Diogo\\Google Drive\\TUDelft\\THESIS\\Code\\MYCODE\\OpenQL\\tools\\metrics')
# 	os.chdir('C:\\Users\\Diogo\\Google Drive\\TUDelft\\THESIS\\Code\\MYCODE\\OpenQL\\tools\\metrics')
# 	openql_manager = importlib.import_module('openql_manager')

# def server():
# 	os.chdir('/home/dmalvalada/bulk/openql_tools/metrics')
# 	import openql_manager

@dataclass
class Gate:
    name: str
    operands: tuple
    cycle: int

def gatelist_from_qasm(qasm):
	gate_list = []
	cycle = 1
	for line in qasm[6:]:
		if not line:
			continue
		if "wait" in line:
			cycle += int(line.replace("wait", ""))
			continue
		if "{" in line:
			gates = line.replace("{ ", "").replace(" }", "").split(" | ")
			for gate in gates:
				name, operands = gate.replace("    ", "").replace("q[", "").replace("]", "").split()
				operands = tuple(map(int, operands.replace("q[", "").replace("]", "").split(",")))
				# gate_list.append({"name" : name, "operands" : operands, "cycle":cycle })
				gate_list.append(Gate(name, operands, cycle))
		else:
			gate = line.replace("    ", "")
			try:
				name, operands = gate.replace("]", "").split(" ")
			except:
				print(gate)
				break
			operands = tuple(map(int, operands.replace("q[", "").replace("]", "").split(",")))
			# gate_list.append({"name" : name, "operands" : operands, "cycle":cycle })
			gate_list.append(Gate(name, operands, cycle))

		cycle += 1
	return gate_list
			
def gatelist_from_file(file):
	with open(file, 'r') as fopen:
		qasm = fopen.read().splitlines()
	return gatelist_from_qasm(qasm)