import matplotlib.pyplot as plt
from qiskit import *
from qiskit.circuit.library import HGate
from qiskit.quantum_info import Statevector

# qc = QuantumCircuit(2)
# qc.append(HGate(), [0])
# qc.append(HGate(), [1])
# qc.draw("mpl")
# plt.show()

# qubits: a, b, sum, carry
qc = QuantumCircuit(4)

# Choose values for A and B:
a = 0
b = 0

# Prepare A and B qubits according to selected values:
if a:
    qc.x(0)
if b:
    qc.x(1)

# XOR (sum) into qubit 2
qc.cx(0, 2)
qc.cx(1, 2)

# AND (carry) into qubit 3
qc.ccx(0, 1, 3)  # a AND b

# measure
# qc.measure_all()

# measurment = qc.cregs[0]

# print(f"Register Name: {measurment.name}")
# print(f"Number of bits: {measurment.size}")

state = Statevector.from_instruction(qc)
print(state)

qc.draw("mpl")
plt.show()