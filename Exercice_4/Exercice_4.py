from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, cr)

# Préparez les qubits en superposition
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])

#000
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])

#001
qc.h(qr[0])
qc.h(qr[1])
qc.z(qr[2])
qc.h(qr[2])

#010
qc.h(qr[0])
qc.h(qr[2])
qc.z(qr[1])
qc.h(qr[1])

#011
qc.h(qr[0])
qc.h(qr[2])
qc.z(qr[1])
qc.h(qr[1])
qc.cx(qr[1], qr[2])

#100
qc.h(qr[1])
qc.h(qr[2])
qc.z(qr[0])
qc.h(qr[0])

#101
qc.h(qr[1])
qc.h(qr[2])
qc.z(qr[0])
qc.h(qr[0])
qc.cx(qr[0], qr[2])

#110
qc.h(qr[1])
qc.h(qr[2])
qc.z(qr[0])
qc.h(qr[0])
qc.cx(qr[0], qr[1])

#111
qc.h(qr[1])
qc.h(qr[2])
qc.z(qr[0])
qc.h(qr[0])
qc.cx(qr[0], qr[1])
qc.cx(qr[0], qr[2])

# Implémentez l'oracle


# Appliquez l'étape de diffusion



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