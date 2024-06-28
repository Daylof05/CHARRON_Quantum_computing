from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(2, 'q')
cr = ClassicalRegister(2, 'c')
qc = QuantumCircuit(qr, cr)

# Appliquez la porte Hadamard au premier qubit
qc.h(qr[0])

# Appliquez la porte CNOT
qc.cx(qr[0], qr[1])

# Ajoutez les mesures
qc.measure(qr, cr)

# Exécutez le circuit sur le simulateur BasicAer
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

# Affichez les résultats
counts = result.get_counts(qc)
print("Résultat de la mesure:", counts)