def shell_sort1(arr):
    gap = len(arr) // 2
    while (gap > 0):
        i = gap
        while i < len(arr):
            temp = arr[i]
            j = i
            while j >= gap and temp < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
            i += 1
        gap //= 2
    return arr


