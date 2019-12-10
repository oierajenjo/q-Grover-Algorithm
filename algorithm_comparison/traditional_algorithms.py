import math
import random
import statistics
import time

import progressbar

from algorithm_comparison import utils


def LinearSearch(lys, element):
    step = 0

    for i in range(len(lys)):
        step = step + 1

        if lys[i] == element:
            return step
    return -1


def BinarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1

    step = 0

    while (first <= last) and (index == -1):

        step = step + 1

        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return step


def JumpSearch(lys, val):
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0

    steps = 0

    while left < length and lys[left] <= val:

        steps = steps + 1

        right = min(length - 1, left + jump)
        if lys[left] <= val <= lys[right]:
            break
        left += jump

    if left >= length or lys[left] > val:
        return -1

    right = min(length - 1, right)
    i = left

    while i <= right and lys[i] <= val:

        steps = steps + 1

        if lys[i] == val:
            return steps
        i += 1

    return -1


def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2

    while fibM < len(lys):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2

    index = -1

    step = 0

    while fibM > 1:

        step = step + 1

        i = min(index + fibM_minus_2, (len(lys) - 1))

        if lys[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i

        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1

        else:
            return step

    if (fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
        return 1

    return -1


def ExponentialSearch(lys, val):
    steps = 0

    if lys[0] == val:
        return 0

    index = 1

    while index < len(lys) and lys[index] <= val:
        steps = steps + 1
        index = index * 2

    return steps + BinarySearch(lys[:min(index, len(lys))], val)


# If x is present in arr[0..n-1], then returns
# index of it, else returns -1
def InterpolationSearch(lys, val):
    # Find indexs of two corners
    lo = 0
    hi = (len(lys) - 1)

    step = 0

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and val >= lys[lo] and val <= lys[hi]:

        step = step + 1

        if lo == hi:
            if lys[lo] == val:
                return lo
            return -1

            # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(((float(hi - lo) /
                         (lys[hi] - lys[lo])) * (val - lys[lo])))

        # Condition of target found
        if lys[pos] == val:
            return step

            # If x is larger, x is in upper part
        if lys[pos] < val:
            lo = pos + 1

            # If x is smaller, x is in lower part
        else:
            hi = pos - 1

    return -1


def test_algorithm(number_list, value, algorithm):
    start_time = time.time()
    steps = algorithm(number_list, value)

    return {
        "time": (time.time() - start_time) * 1000,
        "steps": steps
    }


def performace(n, iterations):
    linear_steps = []
    binary_steps = []
    jump_steps = []
    fib_steps = []
    inter_steps = []
    exponential_steps = []

    linear_time = []
    binary_time = []
    jump_time = []
    fib_time = []
    inter_time = []
    exponential_time = []

    for i in range(1, n + 1):

        print("N = %s" % i)

        bar = progressbar.ProgressBar(max_value=iterations)

        temp_linear_steps = []
        temp_binary_steps = []
        temp_jump_steps = []
        temp_fib_steps = []
        temp_inter_steps = []
        temp_exponential_steps = []

        temp_linear_time = []
        temp_binary_time = []
        temp_jump_time = []
        temp_fib_time = []
        temp_inter_time = []
        temp_exponential_time = []

        for j in range(0, iterations):
            done = False

            while not done:

                # TODO sometimes Interpolation search fails
                try:

                    number_list = utils.random_list(2 ** i)
                    value = number_list[random.randint(0, 2 ** i)]

                    data = test_algorithm(number_list, value, LinearSearch)
                    temp_linear_steps.append(data["steps"])
                    temp_linear_time.append(data["time"])

                    data = test_algorithm(number_list, value, BinarySearch)
                    temp_binary_steps.append(data["steps"])
                    temp_binary_time.append(data["time"])

                    data = test_algorithm(number_list, value, JumpSearch)
                    temp_jump_steps.append(data["steps"])
                    temp_jump_time.append(data["time"])

                    data = test_algorithm(number_list, value, FibonacciSearch)
                    temp_fib_steps.append(data["steps"])
                    temp_fib_time.append(data["time"])

                    data = test_algorithm(number_list, value, InterpolationSearch)
                    temp_inter_steps.append(data["steps"])
                    temp_inter_time.append(data["time"])

                    data = test_algorithm(number_list, value, ExponentialSearch)
                    temp_exponential_steps.append(data["steps"])
                    temp_exponential_time.append(data["time"])

                    done = True
                    bar.update(j)

                except:
                    pass

        linear_steps.append(statistics.mean(temp_linear_steps))
        linear_time.append(statistics.mean(temp_linear_time))

        binary_steps.append(statistics.mean(temp_binary_steps))
        binary_time.append(statistics.mean(temp_binary_time))

        jump_steps.append(statistics.mean(temp_jump_steps))
        jump_time.append(statistics.mean(temp_jump_time))

        fib_steps.append(statistics.mean(temp_fib_steps))
        fib_time.append(statistics.mean(temp_fib_time))

        inter_steps.append(statistics.mean(temp_inter_steps))
        inter_time.append(statistics.mean(temp_inter_time))

        exponential_steps.append(statistics.mean(temp_exponential_steps))
        exponential_time.append(statistics.mean(temp_exponential_time))

    return {
        "linear": {
            "steps": linear_steps,
            "time": linear_time,
        },
        "binary": {
            "steps": binary_steps,
            "time": binary_time,
        },
        "jump": {
            "steps": jump_steps,
            "time": jump_time,
        },
        "fibonacci": {
            "steps": fib_steps,
            "time": fib_time,
        },
        "interpolation": {
            "steps": inter_steps,
            "time": inter_time,
        },
        "exponential": {
            "steps": exponential_steps,
            "time": exponential_time,
        }
    }


def plot_complexity(n):
    data = performace(n)

    time_comp = []
    for i in range(0, n):
        time_comp.append(2 ** i)

    utils.plot("Linear Search", data["linear"]["steps"], time_comp, n)

    time_comp = [0]
    for i in range(1, n):
        time_comp.append(math.log(2 ** i, 10))

    utils.plot("Binary Search", data["binary"]["steps"], time_comp, n)

    time_comp = [0]
    for i in range(1, n):
        time_comp.append(math.sqrt(2 ** i))

    utils.plot("Jump Search", data["jump"]["steps"], time_comp, n)

    time_comp = [0]
    for i in range(1, n):
        time_comp.append(math.log(2 ** i, 10))

    utils.plot("Fibonacci Search", data["fibonacci"]["steps"], time_comp, n)

    time_comp = [0, 0]
    for i in range(2, n):
        time_comp.append(math.log(math.log(2 ** i, 10), 10))

    utils.plot("Interpolation Search", data["interpolation"]["steps"], time_comp, n)

    time_comp = [0]
    for i in range(1, n):
        time_comp.append(math.log(2 ** i, 10))

    utils.plot("Exponential Search", data["exponential"]["steps"], time_comp, n)


if __name__ == '__main__':
    performace(20, 20)
