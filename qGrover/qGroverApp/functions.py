# importing Qiskit
import io
import math

from qiskit import BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# import basic plot tools

def define_circuit(num_qbits, oracle=0):
    k = 1

    # Declaración registros
    qr = QuantumRegister(num_qbits)
    cr = ClassicalRegister(num_qbits)
    # Si estamos usando más de 3 qbits necesitamos un aux para la gate mct
    if num_qbits > 3:
        aux = QuantumRegister(num_qbits - 3)
        groverCircuit = QuantumCircuit(qr, cr, aux)
    else:
        aux = None
        groverCircuit = QuantumCircuit(qr, cr)

    # Hadamard inicial
    groverCircuit.h(qr)

    # Oráculo e inversión de la media

    result = math.pi * math.sqrt((2 ** num_qbits)/k) / 4  # Cálculo de las iteraciones
    iterations = round(result)
    print("Número de iteraciones %d" % iterations)

    # Añadimos oraculo e inversa de la media por iteración
    for i in range(iterations - 1):  # pi * ((2^n)^(1/2))/ 4
        groverCircuit.barrier(qr)
        # Oraculo
        if oracle != 0: groverCircuit.x(qr[oracle])
        groverCircuit.h(qr[num_qbits - 1])
        groverCircuit.mct(qr[0:num_qbits - 1], qr[num_qbits - 1], aux)
        groverCircuit.h(qr[num_qbits - 1])
        if oracle != 0: groverCircuit.x(qr[oracle])

        # Inversa de la media
        groverCircuit.barrier(qr)
        groverCircuit.h(qr)
        groverCircuit.x(qr)
        groverCircuit.h(qr[num_qbits - 1])
        groverCircuit.mct(qr[0:num_qbits - 1], qr[num_qbits - 1], aux)
        groverCircuit.h(qr[num_qbits - 1])
        groverCircuit.x(qr)
        groverCircuit.h(qr)

    groverCircuit.barrier(qr)

    groverCircuit.measure(qr, cr)

    backend = BasicAer.get_backend('qasm_simulator')
    shots = 5000
    results = execute(groverCircuit, backend=backend, shots=shots).result()

    answer = results.get_counts()
    for k in answer.keys():
        answer[k] = answer[k] / shots

    return answer

def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s