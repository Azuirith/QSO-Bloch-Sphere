import matplotlib.pyplot as plt
from qiskit import *
from qiskit.circuit.library import HGate
from qiskit.quantum_info import Statevector
from IPython.display import display
from IPython.display import Latex
from qiskit.visualization import state_visualization
import numpy as np

# qc = QuantumCircuit(2)
# qc.append(HGate(), [0])
# qc.append(HGate(), [1])
# qc.draw("mpl")
# plt.show()

qc = QuantumCircuit(2)

a = 0
# qc.x(a)
# qc.x(a)
# qc.id(a)
# qc.cx(a)
qc.h(a)
qc.y(a)
# qc.z(a)
# qc.rz(np.pi / 2, a)


# measure
# qc.measure_all()

# measurment = qc.cregs[0]

# print(f"Register Name: {measurment.name}")
# print(f"Number of bits: {measurment.size}")
# print(f"Number of bits: {type(measurment)}")
state = Statevector.from_instruction(qc)

print(state.data)
# Determine the angle(theta) from the 1st term
phase = np.angle(state.data[0])
temp = state.data * np.exp(-1j * phase)
# print(f"{temp}")
theta = np.arccos(np.real(temp[0])) * 2

# Determine the phase(phi) of 2nd term
phi = np.angle(temp[1])
print(f"theta = {np.rad2deg(theta)}")
print(f"phi = {phi}")



# ***** This Works ******
# latex =state.draw(output='latex_source')
# fig = plt.figure(figsize=(5, 2))
# fig.text(0.5, 0.5, f"${latex}$", usetex=False)

# qc.draw("mpl")
# plt.show() 