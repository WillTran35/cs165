import csv
import time
import random
from requirements import *
import math
# name of csv
# function array

def uniform_perm(n):
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr

def almost_sorted_perm(n):
    arr = list(range(1, n + 1))
    swaps = math.ceil(math.log2(n))  # log base 2
    for _ in range(swaps):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def two_alternating_runs_perm(n):
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    return odds + evens

# run all the functions 10 times and various sizes 2, 2^16

def run_test(func):
    test_num = [i for i in range(0, 17)]
    res = []
    for i in test_num:
        for j in range(10):
            arr = uniform_perm(2 ** i)
            start = time.perf_counter_ns()
            func(arr)
            end = time.perf_counter_ns()
            elapsed = end - start
            res.append([f'{i}', elapsed])
            print(f"[{i}, {elapsed}]")
    with open(f"{func.__name__}_uniform.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for i in res:
            writer.writerow(i)

    res2 = []
    for i in test_num:
        for j in range(10):
            arr = almost_sorted_perm(2 ** i)
            start = time.perf_counter_ns()
            func(arr)
            end = time.perf_counter_ns()
            elapsed = end - start
            res2.append([f'{i}', elapsed])
            print(f"[{i}, {elapsed}]")
    with open(f"{func.__name__}_almost_sorted.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for i in res2:
            writer.writerow(i)
            # print(f"wrote {i}")

    res3 = []
    for i in test_num:
        for j in range(10):
            arr = two_alternating_runs_perm(2 ** i)
            start = time.perf_counter_ns()
            insertion_sort(arr)
            end = time.perf_counter_ns()
            elapsed = end - start
            res3.append([f'{i}', elapsed])
            print(f"[{i}, {elapsed}]")
    with open(f"{func.__name__}_alt_runs.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for i in res3:
            writer.writerow(i)
            # print(f"wrote {i}")


def test_insertion_sort():
    run_test(insertion_sort)


def test_tim_sort():
    run_test(tim_sort)


def test_shell_sort1():
    run_test(shell_sort1)


def test_shell_sort2():
    run_test(shell_sort2)


def test_shell_sort3():
    run_test(shell_sort3)


def test_shell_sort4():
    run_test(shell_sort4)


def test_shell_sort5():
    run_test(shell_sort5)

if __name__ == "__main__":
    test_insertion_sort()
    test_tim_sort()
    test_shell_sort2()
    test_shell_sort3()
    test_shell_sort4()
    test_shell_sort5()