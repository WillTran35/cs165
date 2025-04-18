from shell_sort2 import shell_sort_main
import math
import random
"""The A083318 sequence, 2k + 1, for k=log n, ..., 3, 2, 1, plus the value 1."""
def compute_gaps(arr):
    start = int(math.log(len(arr)))
    print(start)
    runs = []
    while start > 0:
        runs.append(2*start + 1)
        start -= 1
    runs.append(1)
    return runs

def shell_sort3(arr):
    gaps = compute_gaps(arr)
    return shell_sort_main(arr, gaps)

if __name__ == '__main__':
    arr = [random.randint(1, 4000) for _ in range(100)]
    print(compute_gaps(arr))
    print(shell_sort3(arr))
