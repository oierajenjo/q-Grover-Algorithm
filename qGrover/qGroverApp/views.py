import io

from django.http import HttpResponse
from django.shortcuts import render
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_agg import FigureCanvasAgg

import qGroverApp.functions as functions


# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def demo(request):
    num_qbits = 4
    # result = functions.define_circuit(num_qbits, oracle=1)
    # print(result)
    return render(request, 'demo.html')


def ajax_bar_chart(request):

    if request.method == 'GET':

        if "qubics" in request.GET:
            qubits = int(request.GET["qubics"])
        else:
            qubits = 4

        if "oracle" in request.GET:
            oracle = int(request.GET["oracle"])
        else:
            oracle = 1

        answer = functions.define_circuit(qubits, oracle)

        ordered_answer = OrderedDict(sorted(answer.items()))

        keys = ordered_answer.keys()
        values = ordered_answer.values()

        x = np.arange(len(values))
        index = list(values).index(max(list(values)))
        keys_list = list(keys)
        for i in range(len(keys_list)):
            if i!=index: keys_list[i]=""
        fig, ax = plt.subplots()
        plt.bar(x, values)
        plt.ylabel("Probabilidad")
        plt.xlabel("")
        plt.xticks(x, keys_list)

        svg = functions.pltToSvg()  # convert plot to SVG
        plt.cla()  # clean up plt so it can be re-used
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    else:
        return HttpResponse(status=405)