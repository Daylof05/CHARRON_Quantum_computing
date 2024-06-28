from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, cr)

# Appliquez la porte Hadamard au premier qubit
qc.h(qr[0])

# Appliquez la première porte CNOT
qc.cx(qr[0], qr[1])

# Appliquez la deuxième porte CNOT
qc.cx(qr[1], qr[2])

# Ajoutez les mesures
qc.measure(qr, cr)

# Transpilez et assemblez le circuit pour le simulateur
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Exécutez le circuit
job = simulator.run(qobj)
result = job.result()

# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure :", counts)