from django.shortcuts import render

import numpy as np
import math

import qGroverApp.functions as functions

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def demo(request):
    num_qbits = 4
    result = functions.define_circuit(num_qbits, oracle=1)
    print(result)
    return render(request, 'demo.html')