from shell_sort2 import shell_sort_main
def compute_gaps(arr):
    length = len(arr)
    result = [x for x in range(length,0, -1)]
    return result


def shell_sort5(arr):
    """ sequence, in reverse order, starting from the largest value less than n, down to 1."""
    gaps = compute_gaps(arr)
    return shell_sort_main(arr, gaps)

