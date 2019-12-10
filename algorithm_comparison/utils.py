import random

import matplotlib.pyplot as plt


def random_list(size):
    array = [random.randint(1, 10)]

    for i in range(0, size):
        array.append(array[i] + random.randint(0, 10))

    return array


def plot(title, data, time_comp, n):
    numbers = []

    for i in range(0, n):
        numbers.append(2 ** i)

    fig, ax = plt.subplots()
    plt.title(title)

    ax.plot(numbers, data, label='steps')
    ax.plot(numbers, time_comp, dashes=[6, 2], label='time complexity')

    ax.legend()
    plt.show()


if __name__ == '__main__':
    print(random_list(1024))
