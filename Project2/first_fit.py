from zipzip_tree import ZipZipTree
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
        count += 1

    print(f"assignment {assignment}")
    print(f"buckets: {free_space}")

if __name__ == "__main__":
    arr = [0.1, 0.8, 0.3, 0.5, 0.7, 0.2, 0.6, 0.4]
    first_fit(arr, [], [])
