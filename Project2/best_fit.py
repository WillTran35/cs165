from zipzip_tree import ZipZipTree
from insertion_sort import insertion_sort,tim_sort
def best_fit(items: list[float], assignment: list[int], free_space: list[float]):
    tree = ZipZipTree(len(items))
    count = 0
    for i in items:
        bucket, free = tree.insertForBestFit(i)
        assignment[count] = bucket
        if bucket < len(free_space):
            free_space[bucket] = free
        else:
            free_space.append(free)
        # print(tree.prioq[0])
        count += 1
    print(items)
    print(f"assignment [0, 0, 1, 1, 2, 1, 3, 3] **")
    print(f"assignment {assignment} ACTUAL")
    print(f'buckets: [0.1, 0.0, 0.3, 0.0] **')
    print(f"buckets: {free_space}")

def best_fit_decreasing(items: list[float], assignment: list[int], free_space: list[float]):
    item = list(reversed(tim_sort(items)))
    print(f"BEST FIT DEC {item}")
    # insertion_sort(items).reverse()
    best_fit(item, assignment, free_space)

if __name__ == "__main__":
    items = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
    assignments = [0] * len(items)
    free_space = list()

    best_fit_decreasing(items, assignments, free_space)
    items3 = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
    insertion_sort(items3).reverse()
    print(f"INSERTION SORT: {items3}" )
    # best_fit_decreasing(insertion_sort(items))
    test = [0.83, 0.74, 0.67, 0.64, 0.04, 0.43, 0.63, 0.57, 0.54, 0.53, 0.47, 0.46, 0.36, 0.25, 0.24, 0.23, 0.07, 0.06, 0.05, 0.03]
    assignments2 = [0] * len(items)
    free_space2 = list()
    best_fit(test, assignments2, free_space2)

# [0.13000000000000003,
# 0.010000000000000009,
# 0.019999999999999962,
# 0.0,
# -1.3877787807814457e-17,
# 5.551115123125783e-17,
# -5.551115123125783e-17,
# 0.0]