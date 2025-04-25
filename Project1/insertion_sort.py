import time
def insertion_sort(arr):
    start = time.perf_counter_ns()
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j -1]
            j -= 1
        arr[j] = temp
    end = time.perf_counter_ns()
    return end-start

if __name__ == '__main__':
    x = [1, 4, 0, -1, -5, 6, 3]
    print(insertion_sort(x))
