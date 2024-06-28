from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
qc = QuantumCircuit(qr, cr)

# Appliquez la porte Hadamard au qubit
qc.h(qr[0])

# Ajoutez la mesure
qc.measure(qr, cr)

# Exécutez le circuit sur le simulateur BasicAer
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure:", counts)