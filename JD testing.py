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
# qc.y(a)
qc.h(a)
qc.s(a)
qc.t(a)
# qc.z(a)

# measure
# qc.measure_all()

# measurment = qc.cregs[0]
# print(f"Register Name: {measurment.name}")
# print(f"Number of bits: {measurment.size}")
# print(f"Number of bits: {type(measurment)}")


state = Statevector.from_instruction(qc)

print(state.data)

# Determine global phase of state vector from first term
phase = np.angle(state.data[0])
# Remove global phase from state vector (make 1st term only real)
no_phase = state.data * np.exp(-1j * phase)
# Determine theta from manitude of first term
theta = np.arccos(np.real(no_phase[0])) * 2
# Determine the phase(phi) of 2nd term
phi = np.angle(no_phase[1])

print(f"theta = {np.degrees(theta):.2f}")
print(f"phi = {np.degrees(phi):.2f}")



# ***** This Works ******
latex =state.draw(output='latex_source')
fig = plt.figure(figsize=(5, 2))
fig.text(0.5, 0.5, f"${latex}$", usetex=False)
fig.text(0.5, 0.4, f"$\\theta={np.degrees(theta):.2f}\degree$, $\phi={np.degrees(phi):.2f}\degree$", usetex=False)

plt.show() 