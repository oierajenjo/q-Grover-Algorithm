import math

import matplotlib.pyplot as plt


def GroverSteps(n):
    steps = math.pi * math.sqrt(2 ** n) / 4

    return steps


if __name__ == '__main__':

    steps = []
    numbers = []

    for i in range(0, 20):
        steps.append(GroverSteps(i))
        numbers.append(2 ** i)

    plt.plot(numbers, steps)
    plt.ylabel("pasos")
    plt.xlabel('n')

    plt.title("Grover")
    plt.show()
