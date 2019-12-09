from django.shortcuts import render

import numpy as np
import math

# importing Qiskit
from qiskit import IBMQ, BasicAer, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

# import basic plot tools
from qiskit.visualization import plot_histogram

# Create your views here.


def define_circuit(num_qbits, oracle=0):
    # Declaración registros
    qr = QuantumRegister(num_qbits)
    cr = ClassicalRegister(num_qbits)
    if num_qbits > 3:
        aux = QuantumRegister(num_qbits - 3)
        groverCircuit = QuantumCircuit(qr, cr, aux)
    else:
        aux = QuantumRegister(1)
        groverCircuit = QuantumCircuit(qr, cr, aux)

    # Hadamard inicial
    groverCircuit.h(qr)
    groverCircuit.barrier(qr)

    # Definición del oraculo

    if oracle != 0: groverCircuit.x(qr[oracle])
    groverCircuit.h(qr[num_qbits - 1])
    groverCircuit.mct(qr[0:num_qbits - 1], qr[num_qbits - 1], aux)
    groverCircuit.h(qr[num_qbits - 1])
    if oracle != 0:  groverCircuit.x(qr[oracle])

    # Inversión de la media

    result = math.pi * math.sqrt((2 ** num_qbits)) / 4
    iterations = round(result) + 1

    for i in range(iterations - 1):  # pi * ((2^n)^(1/2))/ 4
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
        answer[k] = answer[k]/shots
    return answer


def inicio(request):
    return render(request, 'inicio.html')

def demo(request):
    num_qbits = 4
    result = define_circuit(num_qbits, oracle=1)
    print(result)
    return render(request, 'demo.html')

