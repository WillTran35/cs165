# Example file: next_fit.py
# explanations for member functions are provided in requirements.py
def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
    # The index i corresponds to the i-th item in items, and assignment[i]
    # specifies the bin number (starting from 0) where the i-th item is placed.

    # free_space: the amount of space left in the jth bin for all j bins created by
    # the algorithm.
    # you should add one element for each bin that the algorithm
    # creates.

    # items - [.5, .7, .5 , .2, .4, .2, .5, .1, .6]
    EPSILON = 1e-10
    print(f"TESTING NEXT FIT {items}")
    count = 0
    for i in items:
        if len(free_space) == 0 or free_space[-1] + EPSILON < i :
            free_space.append(1 - i)
            assignment[count] = len(free_space) - 1
            # assignment.append(len(free_space) - 1)

        else :
            free_space[-1] -= i
            assignment[count] = len(free_space) - 1
            # assignment.append(len(free_space) - 1)
        count += 1
    print(f"NEXT FIT ASSIGNMENT {assignment}")
    print(f"NEXT FIT FREE SPACE {free_space}")


if __name__ == "__main__":
    arr = [.5, .7, .5, .2, .4, .2, .5, .1, .6]

    next_fit(arr, [], [])
