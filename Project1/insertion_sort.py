def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j -1]
            j -= 1
        arr[j] = temp

    return arr

if __name__ == '__main__':
    x = [1, 4, 0, -1, -5, 6, 3]
    print(insertion_sort(x))
