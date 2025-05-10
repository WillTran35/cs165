from zipzip_tree import ZipZipTree
from insertion_sort import insertion_sort, tim_sort
def first_fit(items: list[float], assignment: list[int], free_space: list[float]):
    # The index i corresponds to the i-th item in items, and assignment[i]
    # specifies the bin number (starting from 0) where the i-th item is placed.

    # free_space: the amount of space left in the jth bin for all j bins created by
    # the algorithm.
    # you should add one element for each bin that the algorithm
    # creates.

    tree = ZipZipTree(len(items))
    print(f"TESTING ITEMS: {items}")
    count = 0
    for i in items:
        bucket, free = tree.insertForFirstFit(i)
        assignment[count] = bucket
        if bucket < len(free_space):
            free_space[bucket] = free
        else:
            free_space.append(free)
        # print(tree.prioq[0])
        count += 1

    print(f"assignment {assignment} ACTUAL")
    print("assignment [0, 1, 0, 2, 1, 1, 3, 4, 5, 1, 5, 6, 2, 4, 2, 6, 3, 7, 8, 3] ****")
    print(f"buckets: {free_space}")
    print("expected buckets: [0, 0.01, 0, 0.08, 0.12, 0, 0.01, 0.37, 0.57]")

def first_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    tree = ZipZipTree(len(items))
    sorted_arr = tree.tree_sort_reverse(items)
    print(f"BEST FIT DEC {sorted_arr}")
    print(f"FIRST FIT DEC: {items}")
    first_fit(sorted_arr, assignment, free_space)

if __name__ == "__main__":
    # arr = [0.79, 0.88, 0.95, 0.12, 0.05, 0.46, 0.53, 0.64, 0.04, 0.38,0.03,0.26]
    # first_fit(arr, [0 for i in range(len(arr))], [])
    # print("items: [0.79, 0.88, 0.95, 0.12, 0.05, 0.46, 0.53, 0.64, 0.04, 0.38, 0.03, 0.26]")

    arr2 = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
    # first_fit(arr2, [0 for i in range(len(arr2))], [])
    first_fit_decreasing(arr2, [0 for i in range(len(arr2))], [])

