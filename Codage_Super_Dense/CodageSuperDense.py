from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

#Gestion choix utilisateur
def get_user_choice():
    print("Choisissez les bits à envoyer :")
    print("00")
    print("01")
    print("10")
    print("11")
    choice = input("Entrez votre choix : ")
    return choice

#Préparation des états de Bell
def prepare_bell_state(choice, qr, cr):
    qc = QuantumCircuit(qr, cr)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    
    if choice == '01':
        qc.z(qr[0])
    elif choice == '10':
        qc.x(qr[0])
    elif choice == '11':
        qc.x(qr[0])
        qc.z(qr[0])
    
    ##qc.measure(qr, cr)
    return qc

#Mesure des Qubits
def simulate_circuit(qc):
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    qobj = assemble(compiled_circuit)
    job = simulator.run(qobj)
    result = job.result()
    return result.get_counts(qc)


#Création des registres quantiques et du circuit
def main():
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    
    user_choice = get_user_choice()
    qc = prepare_bell_state(user_choice, qr, cr)
    
    qc.cx(qr[0], qr[1])
    qc.h(qr[0])
    qc.measure(qr, cr)

    counts = simulate_circuit(qc)
    
    states = {'00': '00', '01': '01', '10': '10', '11': '11'}
    state = states.get(user_choice, 'Invalide')
    
    print(f"Résultats de la mesure pour {state} :", counts)

if __name__ == "__main__":
    main()
