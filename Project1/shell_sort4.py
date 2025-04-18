from shell_sort2 import shell_sort_main
from insertion_sort import insertion_sort
import random

"""The A003586 sequence, 2^p * 3^q, 
ordered from the largest such number less than n down to 1."""
def compute_runs(arr):
    gap = set()
    length = len(arr)
    p = 0
    while 2 ** p < length:
        q = 0
        while (3 ** q) * (2 ** p) < length:
            value = (3 ** q) * (2 ** p)
            gap.add(value)

            q += 1

        p += 1
    return list(gap).reverse()


def shell_sort4(arr):
    runs = compute_runs(arr)
    return shell_sort_main(arr, runs)

if __name__ == '__main__':
    arr = [random.randint(1, 4000) for _ in range(100)]
    print(compute_runs(arr))
    print(shell_sort4(arr))