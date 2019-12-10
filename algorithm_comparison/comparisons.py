import matplotlib.pyplot as plt

from algorithm_comparison import traditional_algorithms, grover_algorithm


def compare(n, iterations):
    grover_steps = []
    numbers = []

    for i in range(0, n):
        numbers.append(2 ** i)
        grover_steps.append(grover_algorithm.GroverSteps(i))

    data = traditional_algorithms.performace(n, iterations)

    fig, ax = plt.subplots()
    plt.title("Algorithm Comparison")

    ax.plot(numbers, grover_steps, label='grover')
    # ax.plot(numbers, data["linear"]["steps"], label='linear')
    ax.plot(numbers, data["binary"]["steps"], label='binary')
    # ax.plot(numbers, data["jump"]["steps"], label='jump')
    ax.plot(numbers, data["fibonacci"]["steps"], label='fibonacci')
    ax.plot(numbers, data["interpolation"]["steps"], label='interpolation')
    ax.plot(numbers, data["exponential"]["steps"], label='exponential')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    compare(20, 20)
