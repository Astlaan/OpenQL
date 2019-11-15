from openql import openql as ql
import os
import argparse

def circuit(config_file, new_scheduler='yes', scheduler='ASAP', uniform_sched= 'no', sched_commute = 'yes', mapper='base', moves='no', maptiebreak='random', initial_placement='no', output_dir_name='test_output', optimize='no', measurement=True, log_level='LOG_WARNING'):
	curdir = os.path.dirname(__file__)
	output_dir = os.path.join(curdir, output_dir_name)
	ql.set_option('output_dir', output_dir)
	ql.set_option('optimize', optimize)
	ql.set_option('scheduler', scheduler)
	ql.set_option('scheduler_uniform', uniform_sched)
	ql.set_option('mapper', mapper)
	ql.set_option('initialplace', initial_placement)
	ql.set_option('log_level', log_level)
	ql.set_option('scheduler_post179', new_scheduler)
	ql.set_option('scheduler_commute', sched_commute)
	ql.set_option('mapusemoves', moves)
	ql.set_option('maptiebreak', maptiebreak)

	config_fn = os.path.join(curdir, config_file)

	# platform  = ql.Platform('platform_none', config_fn)
	platform  = ql.Platform('starmon', config_fn)
	sweep_points = [1,2]
	num_circuits = 1
	num_qubits = 16
	p = ql.Program('ising_model_16', platform, num_qubits)
	p.set_sweep_points(sweep_points)
	k = ql.Kernel('ising_model_16', platform, num_qubits)
	k.gate('h',[0])
	k.gate('h',[1])
	k.gate('h',[2])
	k.gate('h',[3])
	k.gate('h',[4])
	k.gate('h',[5])
	k.gate('h',[6])
	k.gate('h',[7])
	k.gate('h',[8])
	k.gate('h',[9])
	k.gate('h',[10])
	k.gate('h',[11])
	k.gate('h',[12])
	k.gate('h',[13])
	k.gate('h',[14])
	k.gate('h',[15])
	k.gate('rz',[0],0,-0.3)
	k.gate('rz',[1],0,0.3)
	k.gate('rz',[1],0,-1.2)
	k.gate('cnot',[0,1])
	k.gate('rz',[1],0,0.6)
	k.gate('cnot',[0,1])
	k.gate('rz',[2],0,-0.36)
	k.gate('rz',[3],0,0.36)
	k.gate('rz',[3],0,-1.44)
	k.gate('cnot',[2,3])
	k.gate('rz',[3],0,0.72)
	k.gate('cnot',[2,3])
	k.gate('rz',[4],0,-0.12)
	k.gate('rz',[5],0,0.12)
	k.gate('rz',[5],0,-0.48)
	k.gate('cnot',[4,5])
	k.gate('rz',[5],0,0.24)
	k.gate('cnot',[4,5])
	k.gate('rz',[6],0,0.22)
	k.gate('rz',[7],0,-0.22)
	k.gate('rz',[7],0,0.88)
	k.gate('cnot',[6,7])
	k.gate('rz',[7],0,-0.44)
	k.gate('cnot',[6,7])
	k.gate('rz',[8],0,0.08)
	k.gate('rz',[9],0,-0.08)
	k.gate('rz',[9],0,0.32)
	k.gate('cnot',[8,9])
	k.gate('rz',[9],0,-0.16)
	k.gate('cnot',[8,9])
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[1],0,0.26)
	k.gate('rz',[2],0,-0.26)
	k.gate('rz',[2],0,1.04)
	k.gate('cnot',[1,2])
	k.gate('rz',[2],0,-0.52)
	k.gate('cnot',[1,2])
	k.gate('rz',[3],0,-0.26)
	k.gate('rz',[4],0,0.26)
	k.gate('rz',[4],0,-1.04)
	k.gate('cnot',[3,4])
	k.gate('rz',[4],0,0.52)
	k.gate('cnot',[3,4])
	k.gate('rz',[5],0,0.38)
	k.gate('rz',[6],0,-0.38)
	k.gate('rz',[6],0,1.52)
	k.gate('cnot',[5,6])
	k.gate('rz',[6],0,-0.76)
	k.gate('cnot',[5,6])
	k.gate('rz',[7],0,-0.26)
	k.gate('rz',[8],0,0.26)
	k.gate('rz',[8],0,-1.04)
	k.gate('cnot',[7,8])
	k.gate('rz',[8],0,0.52)
	k.gate('cnot',[7,8])
	k.gate('rz',[9],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('h',[0])
	k.gate('rz',[0],0,-1.92)
	k.gate('h',[0])
	k.gate('h',[1])
	k.gate('rz',[1],0,-1.92)
	k.gate('h',[1])
	k.gate('h',[2])
	k.gate('rz',[2],0,-1.92)
	k.gate('h',[2])
	k.gate('h',[3])
	k.gate('rz',[3],0,-1.92)
	k.gate('h',[3])
	k.gate('h',[4])
	k.gate('rz',[4],0,-1.92)
	k.gate('h',[4])
	k.gate('h',[5])
	k.gate('rz',[5],0,-1.92)
	k.gate('h',[5])
	k.gate('h',[6])
	k.gate('rz',[6],0,-1.92)
	k.gate('h',[6])
	k.gate('h',[7])
	k.gate('rz',[7],0,-1.92)
	k.gate('h',[7])
	k.gate('h',[8])
	k.gate('rz',[8],0,-1.92)
	k.gate('h',[8])
	k.gate('h',[9])
	k.gate('rz',[9],0,-1.92)
	k.gate('h',[9])
	k.gate('h',[10])
	k.gate('rz',[10],0,-1.92)
	k.gate('h',[10])
	k.gate('h',[11])
	k.gate('rz',[11],0,-1.92)
	k.gate('h',[11])
	k.gate('h',[12])
	k.gate('rz',[12],0,-1.92)
	k.gate('h',[12])
	k.gate('h',[13])
	k.gate('rz',[13],0,-1.92)
	k.gate('h',[13])
	k.gate('h',[14])
	k.gate('rz',[14],0,-1.92)
	k.gate('h',[14])
	k.gate('h',[15])
	k.gate('rz',[15],0,-1.92)
	k.gate('h',[15])
	k.gate('rz',[0],0,-0.288)
	k.gate('rz',[1],0,0.864)
	k.gate('rz',[2],0,1.152)
	k.gate('rz',[3],0,-1.056)
	k.gate('rz',[4],0,-1.44)
	k.gate('rz',[5],0,-0.576)
	k.gate('rz',[6],0,1.536)
	k.gate('rz',[7],0,-0.288)
	k.gate('rz',[8],0,1.248)
	k.gate('rz',[9],0,-1.824)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[0],0,-0.9)
	k.gate('rz',[1],0,0.9)
	k.gate('rz',[1],0,-3.6)
	k.gate('cnot',[0,1])
	k.gate('rz',[1],0,1.8)
	k.gate('cnot',[0,1])
	k.gate('rz',[2],0,-1.08)
	k.gate('rz',[3],0,1.08)
	k.gate('rz',[3],0,-4.32)
	k.gate('cnot',[2,3])
	k.gate('rz',[3],0,2.16)
	k.gate('cnot',[2,3])
	k.gate('rz',[4],0,-0.36)
	k.gate('rz',[5],0,0.36)
	k.gate('rz',[5],0,-1.44)
	k.gate('cnot',[4,5])
	k.gate('rz',[5],0,0.72)
	k.gate('cnot',[4,5])
	k.gate('rz',[6],0,0.66)
	k.gate('rz',[7],0,-0.66)
	k.gate('rz',[7],0,2.64)
	k.gate('cnot',[6,7])
	k.gate('rz',[7],0,-1.32)
	k.gate('cnot',[6,7])
	k.gate('rz',[8],0,0.24)
	k.gate('rz',[9],0,-0.24)
	k.gate('rz',[9],0,0.96)
	k.gate('cnot',[8,9])
	k.gate('rz',[9],0,-0.48)
	k.gate('cnot',[8,9])
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[1],0,0.78)
	k.gate('rz',[2],0,-0.78)
	k.gate('rz',[2],0,3.12)
	k.gate('cnot',[1,2])
	k.gate('rz',[2],0,-1.56)
	k.gate('cnot',[1,2])
	k.gate('rz',[3],0,-0.78)
	k.gate('rz',[4],0,0.78)
	k.gate('rz',[4],0,-3.12)
	k.gate('cnot',[3,4])
	k.gate('rz',[4],0,1.56)
	k.gate('cnot',[3,4])
	k.gate('rz',[5],0,1.14)
	k.gate('rz',[6],0,-1.14)
	k.gate('rz',[6],0,4.56)
	k.gate('cnot',[5,6])
	k.gate('rz',[6],0,-2.28)
	k.gate('cnot',[5,6])
	k.gate('rz',[7],0,-0.78)
	k.gate('rz',[8],0,0.78)
	k.gate('rz',[8],0,-3.12)
	k.gate('cnot',[7,8])
	k.gate('rz',[8],0,1.56)
	k.gate('cnot',[7,8])
	k.gate('rz',[9],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('h',[0])
	k.gate('rz',[0],0,-0.96)
	k.gate('h',[0])
	k.gate('h',[1])
	k.gate('rz',[1],0,-0.96)
	k.gate('h',[1])
	k.gate('h',[2])
	k.gate('rz',[2],0,-0.96)
	k.gate('h',[2])
	k.gate('h',[3])
	k.gate('rz',[3],0,-0.96)
	k.gate('h',[3])
	k.gate('h',[4])
	k.gate('rz',[4],0,-0.96)
	k.gate('h',[4])
	k.gate('h',[5])
	k.gate('rz',[5],0,-0.96)
	k.gate('h',[5])
	k.gate('h',[6])
	k.gate('rz',[6],0,-0.96)
	k.gate('h',[6])
	k.gate('h',[7])
	k.gate('rz',[7],0,-0.96)
	k.gate('h',[7])
	k.gate('h',[8])
	k.gate('rz',[8],0,-0.96)
	k.gate('h',[8])
	k.gate('h',[9])
	k.gate('rz',[9],0,-0.96)
	k.gate('h',[9])
	k.gate('h',[10])
	k.gate('rz',[10],0,-0.96)
	k.gate('h',[10])
	k.gate('h',[11])
	k.gate('rz',[11],0,-0.96)
	k.gate('h',[11])
	k.gate('h',[12])
	k.gate('rz',[12],0,-0.96)
	k.gate('h',[12])
	k.gate('h',[13])
	k.gate('rz',[13],0,-0.96)
	k.gate('h',[13])
	k.gate('h',[14])
	k.gate('rz',[14],0,-0.96)
	k.gate('h',[14])
	k.gate('h',[15])
	k.gate('rz',[15],0,-0.96)
	k.gate('h',[15])
	k.gate('rz',[0],0,-0.144)
	k.gate('rz',[1],0,0.432)
	k.gate('rz',[2],0,0.576)
	k.gate('rz',[3],0,-0.528)
	k.gate('rz',[4],0,-0.72)
	k.gate('rz',[5],0,-0.288)
	k.gate('rz',[6],0,0.768)
	k.gate('rz',[7],0,-0.144)
	k.gate('rz',[8],0,0.624)
	k.gate('rz',[9],0,-0.912)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[0],0,-1.5)
	k.gate('rz',[1],0,1.5)
	k.gate('rz',[1],0,-6)
	k.gate('cnot',[0,1])
	k.gate('rz',[1],0,3)
	k.gate('cnot',[0,1])
	k.gate('rz',[2],0,-1.8)
	k.gate('rz',[3],0,1.8)
	k.gate('rz',[3],0,-7.2)
	k.gate('cnot',[2,3])
	k.gate('rz',[3],0,3.6)
	k.gate('cnot',[2,3])
	k.gate('rz',[4],0,-0.6)
	k.gate('rz',[5],0,0.6)
	k.gate('rz',[5],0,-2.4)
	k.gate('cnot',[4,5])
	k.gate('rz',[5],0,1.2)
	k.gate('cnot',[4,5])
	k.gate('rz',[6],0,1.1)
	k.gate('rz',[7],0,-1.1)
	k.gate('rz',[7],0,4.4)
	k.gate('cnot',[6,7])
	k.gate('rz',[7],0,-2.2)
	k.gate('cnot',[6,7])
	k.gate('rz',[8],0,0.4)
	k.gate('rz',[9],0,-0.4)
	k.gate('rz',[9],0,1.6)
	k.gate('cnot',[8,9])
	k.gate('rz',[9],0,-0.8)
	k.gate('cnot',[8,9])
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[1],0,1.3)
	k.gate('rz',[2],0,-1.3)
	k.gate('rz',[2],0,5.2)
	k.gate('cnot',[1,2])
	k.gate('rz',[2],0,-2.6)
	k.gate('cnot',[1,2])
	k.gate('rz',[3],0,-1.3)
	k.gate('rz',[4],0,1.3)
	k.gate('rz',[4],0,-5.2)
	k.gate('cnot',[3,4])
	k.gate('rz',[4],0,2.6)
	k.gate('cnot',[3,4])
	k.gate('rz',[5],0,1.9)
	k.gate('rz',[6],0,-1.9)
	k.gate('rz',[6],0,7.6)
	k.gate('cnot',[5,6])
	k.gate('rz',[6],0,-3.8)
	k.gate('cnot',[5,6])
	k.gate('rz',[7],0,-1.3)
	k.gate('rz',[8],0,1.3)
	k.gate('rz',[8],0,-5.2)
	k.gate('cnot',[7,8])
	k.gate('rz',[8],0,2.6)
	k.gate('cnot',[7,8])
	k.gate('rz',[9],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('h',[0])
	k.gate('rz',[0],0,-0)
	k.gate('h',[0])
	k.gate('h',[1])
	k.gate('rz',[1],0,-0)
	k.gate('h',[1])
	k.gate('h',[2])
	k.gate('rz',[2],0,-0)
	k.gate('h',[2])
	k.gate('h',[3])
	k.gate('rz',[3],0,-0)
	k.gate('h',[3])
	k.gate('h',[4])
	k.gate('rz',[4],0,-0)
	k.gate('h',[4])
	k.gate('h',[5])
	k.gate('rz',[5],0,-0)
	k.gate('h',[5])
	k.gate('h',[6])
	k.gate('rz',[6],0,-0)
	k.gate('h',[6])
	k.gate('h',[7])
	k.gate('rz',[7],0,-0)
	k.gate('h',[7])
	k.gate('h',[8])
	k.gate('rz',[8],0,-0)
	k.gate('h',[8])
	k.gate('h',[9])
	k.gate('rz',[9],0,-0)
	k.gate('h',[9])
	k.gate('h',[10])
	k.gate('rz',[10],0,-0)
	k.gate('h',[10])
	k.gate('h',[11])
	k.gate('rz',[11],0,-0)
	k.gate('h',[11])
	k.gate('h',[12])
	k.gate('rz',[12],0,-0)
	k.gate('h',[12])
	k.gate('h',[13])
	k.gate('rz',[13],0,-0)
	k.gate('h',[13])
	k.gate('h',[14])
	k.gate('rz',[14],0,-0)
	k.gate('h',[14])
	k.gate('h',[15])
	k.gate('rz',[15],0,-0)
	k.gate('h',[15])
	k.gate('rz',[0],0,-0)
	k.gate('rz',[1],0,0)
	k.gate('rz',[2],0,0)
	k.gate('rz',[3],0,-0)
	k.gate('rz',[4],0,-0)
	k.gate('rz',[5],0,-0)
	k.gate('rz',[6],0,0)
	k.gate('rz',[7],0,-0)
	k.gate('rz',[8],0,0)
	k.gate('rz',[9],0,-0)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[0],0,-2.1)
	k.gate('rz',[1],0,2.1)
	k.gate('rz',[1],0,-8.4)
	k.gate('cnot',[0,1])
	k.gate('rz',[1],0,4.2)
	k.gate('cnot',[0,1])
	k.gate('rz',[2],0,-2.52)
	k.gate('rz',[3],0,2.52)
	k.gate('rz',[3],0,-10.08)
	k.gate('cnot',[2,3])
	k.gate('rz',[3],0,5.04)
	k.gate('cnot',[2,3])
	k.gate('rz',[4],0,-0.84)
	k.gate('rz',[5],0,0.84)
	k.gate('rz',[5],0,-3.36)
	k.gate('cnot',[4,5])
	k.gate('rz',[5],0,1.68)
	k.gate('cnot',[4,5])
	k.gate('rz',[6],0,1.54)
	k.gate('rz',[7],0,-1.54)
	k.gate('rz',[7],0,6.16)
	k.gate('cnot',[6,7])
	k.gate('rz',[7],0,-3.08)
	k.gate('cnot',[6,7])
	k.gate('rz',[8],0,0.56)
	k.gate('rz',[9],0,-0.56)
	k.gate('rz',[9],0,2.24)
	k.gate('cnot',[8,9])
	k.gate('rz',[9],0,-1.12)
	k.gate('cnot',[8,9])
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[1],0,1.82)
	k.gate('rz',[2],0,-1.82)
	k.gate('rz',[2],0,7.28)
	k.gate('cnot',[1,2])
	k.gate('rz',[2],0,-3.64)
	k.gate('cnot',[1,2])
	k.gate('rz',[3],0,-1.82)
	k.gate('rz',[4],0,1.82)
	k.gate('rz',[4],0,-7.28)
	k.gate('cnot',[3,4])
	k.gate('rz',[4],0,3.64)
	k.gate('cnot',[3,4])
	k.gate('rz',[5],0,2.66)
	k.gate('rz',[6],0,-2.66)
	k.gate('rz',[6],0,10.64)
	k.gate('cnot',[5,6])
	k.gate('rz',[6],0,-5.32)
	k.gate('cnot',[5,6])
	k.gate('rz',[7],0,-1.82)
	k.gate('rz',[8],0,1.82)
	k.gate('rz',[8],0,-7.28)
	k.gate('cnot',[7,8])
	k.gate('rz',[8],0,3.64)
	k.gate('cnot',[7,8])
	k.gate('rz',[9],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('h',[0])
	k.gate('rz',[0],0,0.96)
	k.gate('h',[0])
	k.gate('h',[1])
	k.gate('rz',[1],0,0.96)
	k.gate('h',[1])
	k.gate('h',[2])
	k.gate('rz',[2],0,0.96)
	k.gate('h',[2])
	k.gate('h',[3])
	k.gate('rz',[3],0,0.96)
	k.gate('h',[3])
	k.gate('h',[4])
	k.gate('rz',[4],0,0.96)
	k.gate('h',[4])
	k.gate('h',[5])
	k.gate('rz',[5],0,0.96)
	k.gate('h',[5])
	k.gate('h',[6])
	k.gate('rz',[6],0,0.96)
	k.gate('h',[6])
	k.gate('h',[7])
	k.gate('rz',[7],0,0.96)
	k.gate('h',[7])
	k.gate('h',[8])
	k.gate('rz',[8],0,0.96)
	k.gate('h',[8])
	k.gate('h',[9])
	k.gate('rz',[9],0,0.96)
	k.gate('h',[9])
	k.gate('h',[10])
	k.gate('rz',[10],0,0.96)
	k.gate('h',[10])
	k.gate('h',[11])
	k.gate('rz',[11],0,0.96)
	k.gate('h',[11])
	k.gate('h',[12])
	k.gate('rz',[12],0,0.96)
	k.gate('h',[12])
	k.gate('h',[13])
	k.gate('rz',[13],0,0.96)
	k.gate('h',[13])
	k.gate('h',[14])
	k.gate('rz',[14],0,0.96)
	k.gate('h',[14])
	k.gate('h',[15])
	k.gate('rz',[15],0,0.96)
	k.gate('h',[15])
	k.gate('rz',[0],0,0.144)
	k.gate('rz',[1],0,-0.432)
	k.gate('rz',[2],0,-0.576)
	k.gate('rz',[3],0,0.528)
	k.gate('rz',[4],0,0.72)
	k.gate('rz',[5],0,0.288)
	k.gate('rz',[6],0,-0.768)
	k.gate('rz',[7],0,0.144)
	k.gate('rz',[8],0,-0.624)
	k.gate('rz',[9],0,0.912)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[0],0,-2.7)
	k.gate('rz',[1],0,2.7)
	k.gate('rz',[1],0,-10.8)
	k.gate('cnot',[0,1])
	k.gate('rz',[1],0,5.4)
	k.gate('cnot',[0,1])
	k.gate('rz',[2],0,-3.24)
	k.gate('rz',[3],0,3.24)
	k.gate('rz',[3],0,-12.96)
	k.gate('cnot',[2,3])
	k.gate('rz',[3],0,6.48)
	k.gate('cnot',[2,3])
	k.gate('rz',[4],0,-1.08)
	k.gate('rz',[5],0,1.08)
	k.gate('rz',[5],0,-4.32)
	k.gate('cnot',[4,5])
	k.gate('rz',[5],0,2.16)
	k.gate('cnot',[4,5])
	k.gate('rz',[6],0,1.98)
	k.gate('rz',[7],0,-1.98)
	k.gate('rz',[7],0,7.92)
	k.gate('cnot',[6,7])
	k.gate('rz',[7],0,-3.96)
	k.gate('cnot',[6,7])
	k.gate('rz',[8],0,0.72)
	k.gate('rz',[9],0,-0.72)
	k.gate('rz',[9],0,2.88)
	k.gate('cnot',[8,9])
	k.gate('rz',[9],0,-1.44)
	k.gate('cnot',[8,9])
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[11],0,-1)
	k.gate('cnot',[10,11])
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[13],0,-1)
	k.gate('cnot',[12,13])
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[15],0,-1)
	k.gate('cnot',[14,15])
	k.gate('rz',[1],0,2.34)
	k.gate('rz',[2],0,-2.34)
	k.gate('rz',[2],0,9.36)
	k.gate('cnot',[1,2])
	k.gate('rz',[2],0,-4.68)
	k.gate('cnot',[1,2])
	k.gate('rz',[3],0,-2.34)
	k.gate('rz',[4],0,2.34)
	k.gate('rz',[4],0,-9.36)
	k.gate('cnot',[3,4])
	k.gate('rz',[4],0,4.68)
	k.gate('cnot',[3,4])
	k.gate('rz',[5],0,3.42)
	k.gate('rz',[6],0,-3.42)
	k.gate('rz',[6],0,13.68)
	k.gate('cnot',[5,6])
	k.gate('rz',[6],0,-6.84)
	k.gate('cnot',[5,6])
	k.gate('rz',[7],0,-2.34)
	k.gate('rz',[8],0,2.34)
	k.gate('rz',[8],0,-9.36)
	k.gate('cnot',[7,8])
	k.gate('rz',[8],0,4.68)
	k.gate('cnot',[7,8])
	k.gate('rz',[9],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[10],0,-1)
	k.gate('cnot',[9,10])
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[12],0,-1)
	k.gate('cnot',[11,12])
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('rz',[14],0,-1)
	k.gate('cnot',[13,14])
	k.gate('h',[0])
	k.gate('rz',[0],0,1.92)
	k.gate('h',[0])
	k.gate('h',[1])
	k.gate('rz',[1],0,1.92)
	k.gate('h',[1])
	k.gate('h',[2])
	k.gate('rz',[2],0,1.92)
	k.gate('h',[2])
	k.gate('h',[3])
	k.gate('rz',[3],0,1.92)
	k.gate('h',[3])
	k.gate('h',[4])
	k.gate('rz',[4],0,1.92)
	k.gate('h',[4])
	k.gate('h',[5])
	k.gate('rz',[5],0,1.92)
	k.gate('h',[5])
	k.gate('h',[6])
	k.gate('rz',[6],0,1.92)
	k.gate('h',[6])
	k.gate('h',[7])
	k.gate('rz',[7],0,1.92)
	k.gate('h',[7])
	k.gate('h',[8])
	k.gate('rz',[8],0,1.92)
	k.gate('h',[8])
	k.gate('h',[9])
	k.gate('rz',[9],0,1.92)
	k.gate('h',[9])
	k.gate('h',[10])
	k.gate('rz',[10],0,1.92)
	k.gate('h',[10])
	k.gate('h',[11])
	k.gate('rz',[11],0,1.92)
	k.gate('h',[11])
	k.gate('h',[12])
	k.gate('rz',[12],0,1.92)
	k.gate('h',[12])
	k.gate('h',[13])
	k.gate('rz',[13],0,1.92)
	k.gate('h',[13])
	k.gate('h',[14])
	k.gate('rz',[14],0,1.92)
	k.gate('h',[14])
	k.gate('h',[15])
	k.gate('rz',[15],0,1.92)
	k.gate('h',[15])
	k.gate('rz',[0],0,0.288)
	k.gate('rz',[1],0,-0.864)
	k.gate('rz',[2],0,-1.152)
	k.gate('rz',[3],0,1.056)
	k.gate('rz',[4],0,1.44)
	k.gate('rz',[5],0,0.576)
	k.gate('rz',[6],0,-1.536)
	k.gate('rz',[7],0,0.288)
	k.gate('rz',[8],0,-1.248)
	k.gate('rz',[9],0,1.824)
	k.gate('rz',[10],0,-1)
	k.gate('rz',[11],0,-1)
	k.gate('rz',[12],0,-1)
	k.gate('rz',[13],0,-1)
	k.gate('rz',[14],0,-1)
	k.gate('rz',[15],0,-1)

	if measurement:
		 for q in range(num_qubits):
				k.gate('measure', [q])

	p.add_kernel(k)
	p.compile()
	ql.set_option('mapper', 'no')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='OpenQL compilation of a Quantum Algorithm')
	parser.add_argument('config_file', help='Path to the OpenQL configuration file to compile this algorithm')
	parser.add_argument('--new_scheduler', nargs='?', default='yes', help='Scheduler defined by Hans')
	parser.add_argument('--scheduler', nargs='?', default='ASAP', help='Scheduler specification (ASAP (default), ALAP, ...)')
	parser.add_argument('--uniform_sched', nargs='?', default='no', help='Uniform shceduler actication (yes or no)')
	parser.add_argument('--sched_commute', nargs='?', default='yes', help='Permits two-qubit gates to be commutable')
	parser.add_argument('--mapper', nargs='?', default='base', help='Mapper specification (base, minextend, minextendrc)')
	parser.add_argument('--moves', nargs='?', default='no', help='Let the use of moves')
	parser.add_argument('--maptiebreak', nargs='?', default='random', help='')
	parser.add_argument('--initial_placement', nargs='?', default='no', help='Initial placement specification (yes or no)')
	parser.add_argument('--out_dir', nargs='?', default='test_output', help='Folder name to store the compilation')
	parser.add_argument('--measurement', nargs='?', default=True, help='Add measurement to all the qubits in the end of the algorithm')
	args = parser.parse_args()
	try:
		 circuit(args.config_file, args.new_scheduler, args.scheduler, args.uniform_sched, args.sched_commute, args.mapper, args.moves, args.maptiebreak, args.initial_placement, args.out_dir)
	except TypeError:
		 print('\nCompiled, but some gate is not defined in the configuration file. \nThe gate will be invoked like it is.')
		 raise