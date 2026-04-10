import matplotlib.pyplot as plt
from qiskit import *
from qiskit.quantum_info import Statevector
import numpy as np

# *** Quantum Circuit ***
# Initialize a new quantum circuit object with one qubit
qc = QuantumCircuit(1)

# Apply quantum gates
a = 0
qc.h(a)     # Hadamard Gate -> creates a superposition state
qc.s(a)     # Clifford gate S Gate -> adds a phase of pi/2
qc.t(a)     # T Gate -> adds a phase shift of 1/4 pi to the 1 state


# *** Determine State Vector ***
# Obtain statevector object from quantum circuit
state = Statevector.from_instruction(qc)

# Determine global phase of state vector from first term
phase = np.angle(state.data[0])
# Remove global phase from state vector (make 1st term only real)
no_phase = state.data * np.exp(-1j * phase)

# Determine theta from magnitude of first term
theta = np.arccos(np.real(no_phase[0])) * 2

# Determine the phase (phi) of 2nd term
phi = np.angle(no_phase[1])

# Display state vector to terminal
print(state.data)
print(f"theta = {np.degrees(theta):.2f}")
print(f"phi = {np.degrees(phi):.2f}")


# *** Visual Display ***
# Obtain a latex IPython Latex object from statevector
latex = state.draw(output = 'latex_source')
# Create a new matplotlib figure
fig = plt.figure(figsize = (6, 2.5))
# Add text to figure to display the resulting quantum 
# state vector as well as its corresponding spherical cordinates
fig.text(0.5, 0.5, f"${latex}$", ha='center', fontsize = 14, usetex = False)
fig.text(0.5, 0.3, fr"$\theta={np.degrees(theta):.2f}\degree$, $\phi={np.degrees(phi):.2f}\degree$", fontsize = 12, ha='center', usetex = False)

plt.show()