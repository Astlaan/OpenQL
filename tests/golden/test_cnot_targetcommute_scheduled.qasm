version 1.0
# this file has been automatically generated by the OpenQL compiler please do not modify it manually.
qubits 7
.aKernel

    cnot q[5],q[3]
    wait 3
    { cnot q[1],q[3] | t q[5] }
    wait 2
    y q[5]
    { cnot q[6],q[3] | t q[1] | t q[5] }
    wait 2
    { y q[1] | y q[5] }
    { cnot q[0],q[3] | t q[6] | t q[1] | t q[5] }
    wait 2
    { y q[6] | y q[1] | y q[5] }
