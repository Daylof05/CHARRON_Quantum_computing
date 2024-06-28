from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import numpy as np
from matplotlib import pyplot as plt

#Gestion choix utilisateur
def get_user_choice():
    print("Choisissez la porte à appliquer :")
    print("H")
    print("X")
    print("Y")
    print("Z")
    choice = input("Entrez votre choix : ")
    return choice


#Préparation d'un état arbitraire
def prepare_arbitrary_state(a, b):
    """
    Prepare un qubit dans l'état a|0> + b|1>.
    a et b doivent être des nombres complexes
    """
    qc = QuantumCircuit(1)

    #Normaliser les coefficient
    norm = np.sqrt(np.abs(a)**2 + np.abs(b)**2)
    a = a / norm
    b = b / norm

    #Calcul des angles de rotation
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b) - np.angle(a)

    #Application des rotations necéssaires
    qc.ry(theta, 0)
    qc.rz(phi, 0)
    return qc


#Visualisation sur la sphère de Blosch
def visualization_bloch(choice, qc):
    if choice == 'H':
        qc.h(0)
    elif choice == 'X':
        qc.x(0)
    elif choice == 'Y':
        qc.y(0)
    elif choice == 'Z':
        qc.z(0)
    else:
        print("Choix invalide")
        return

    state = Statevector.from_instruction(qc)
    plot_bloch_multivector(state)
    plt.title(f"Après porte {choice}")
    plt.show()

def main():
    user_choice = get_user_choice()
    qc = prepare_arbitrary_state(1 + 2j, 3 + 4j)
    state = Statevector.from_instruction(qc)
    plot_bloch_multivector(state)
    plt.title(f"Qubit")
    plt.show()
    visualization_bloch(user_choice, qc)

if __name__ == "__main__":
    main()