import random


def random_list(size):
    array = [random.randint(1, 10)]

    for i in range(0, size):
        array.append(array[i] + random.randint(0, 10))

    return array


if __name__ == '__main__':
    print(random_list(1024))
