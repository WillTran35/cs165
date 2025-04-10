# The sequence, 2[n/2^(k+1)]+1, for k=1,2,...,log n,
# where [*] denotes the floor function.
import random
def compute_runs(arr):
    # ex: length 6
    length = len(arr)
    runs = []
    k = 1
    gap = 2 * int(length / 2 ** (k + 1)) + 1

    while gap > 1:
        runs.append(gap)
        k += 1
        gap = 2 * int(length / 2 ** (k + 1)) + 1
        # print(f"runs {runs}")
    if gap == 1:
        runs.append(1)
    return runs


def shell_sort_main(arr, gap):
    index = 0
    start = gap[index]

    while start > 0 and index < len(gap):
        i = start
        while i < len(arr):
            temp = arr[i]
            j = i
            while j >= start and temp < arr[j - start]:
                arr[j] = arr[j - start]
                j -= start
            arr[j] = temp
            i += 1
        index += 1
        if index >= len(gap):
            break
        start = gap[index]
    return arr

def shell_sort2(arr):
    runs = compute_runs(arr)
    return shell_sort_main(arr, runs)

if __name__ == '__main__':
    arr = [random.randint(1, 4000) for _ in range(11)]
    print(compute_runs(arr))
    print(shell_sort2(arr))
