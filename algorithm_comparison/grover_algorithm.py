import math

import matplotlib.pyplot as plt


def GroverSteps(n):
    steps = math.pi * math.sqrt(2 ** n) / 4

    return steps


def GroverStepsMultiple(n, k):
    steps = math.pi * math.sqrt((2 ** n) / k) / 4

    return steps


if __name__ == '__main__':

    steps = []
    numbers = []

    for i in range(1, 100):
        steps.append(GroverStepsMultiple(20, i))
        numbers.append(i)

    plt.plot(numbers, steps)
    plt.ylabel("pasos")
    plt.xlabel('numero de variables')

    plt.title("Grover (n = 20)")
    plt.show()
