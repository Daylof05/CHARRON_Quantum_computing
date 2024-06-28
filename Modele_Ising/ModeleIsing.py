import numpy as np
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

nbQubit = 5
nbRota = 0.1
steps= 4

qr = QuantumRegister(nbQubit, 'q')
cr = ClassicalRegister(nbQubit, 'c')
qc = QuantumCircuit(qr, cr)

for i in range(nbQubit):
    qc.h(qr[i])


for i in range(steps):
    for i in range(nbQubit):
        qc.cx(qr[i-1], qr[i])
        qc.rz(nbRota,qr[i])

qc.measure(qr, cr)
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()
counts = result.get_counts(qc)
print("Résultats de la mesure:", counts)