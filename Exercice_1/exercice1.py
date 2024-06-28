from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
qc = QuantumCircuit(qr, cr)

# Appliquez la porte Hadamard au qubit
qc.h(qr[0])

# Ajoutez une mesure
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