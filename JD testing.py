import matplotlib.pyplot as plt
from qiskit import *
from qiskit.circuit.library import HGate
from qiskit.quantum_info import Statevector
from IPython.display import display
from IPython.display import Latex
from qiskit.visualization import state_visualization

# qc = QuantumCircuit(2)
# qc.append(HGate(), [0])
# qc.append(HGate(), [1])
# qc.draw("mpl")
# plt.show()

# qubits: a, b, sum, carry
qc = QuantumCircuit(1)

# Choose values for A and B:
a = 0

qc.h(a)
qc.h(a)


# measure
# qc.measure_all()

# measurment = qc.cregs[0]

# print(f"Register Name: {measurment.name}")
# print(f"Number of bits: {measurment.size}")
# print(f"Number of bits: {type(measurment)}")

state = Statevector.from_instruction(qc)
print(state)
latex =state.draw(output='latex')
# state_to_latex = state_visualization._state_to_latex_ket(state.data, max_size = 128)


# latex(state_to_latex)
fig, ax = plt.subplots(figsize=(5, 2))
ax.text(0.5, 0.5, f"{latex}")
ax.axis('off')

# qc.draw("mpl")
plt.show() 