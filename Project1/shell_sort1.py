import random
import time
from shell_sort2 import shell_sort_main
def compute_runs(arr):
    length = len(arr)
    runs = []
    gap = length // 2

    while gap > 1:
        runs.append(gap)
        gap //= 2
        # print(f"runs {runs}")
    if gap == 1:
        runs.append(1)
    return runs

def shell_sort1(arr):
    runs = compute_runs(arr)
    return shell_sort_main(arr, runs)

if __name__ == '__main__':
    arr = [random.randint(1, 4000) for _ in range(11)]
    print(compute_runs(arr))
    print(shell_sort1(arr))


