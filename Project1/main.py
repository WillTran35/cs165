from requirements import *
import random

if __name__ == "__main__":
    x = [1, 4, 0, -1, -5, 6, 3]
    arr = [random.randint(1, 100) for _ in range(10)]
    arr2 = [random.randint(1, 100) for _ in range(20)]
    arr3 = [random.randint(1, 100) for _ in range(30)]
    arr4 = [random.randint(1, 100) for _ in range(40)]



    print(f"Insertion sort: {insertion_sort(x)}")
    print(f"Tim_sort: {tim_sort(x)}")
    print(f"Shell sort: {shell_sort1(x)}")

