from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, cr)

# Préparez les qubits pour la téléportation quantique
qc.h(qr[1])
qc.cx(qr[1], qr[2])

#qc.cx(qr[0], qr[1])
qc.h(qr[0])

# Appliquez les mesures nécessaires
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

# Appliquez les opérations conditionnelles
if cr[1] == 1:
    qc.x(qr[2])

if cr[0] == 1:
    qc.z(qr[2])

# Transpilez et assemblez le circuit pour le simulateur
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Exécutez le circuit
job = simulator.run(qobj)
result = job.result()

# Affichez le code QASM et les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure :", counts)