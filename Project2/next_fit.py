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
    index = 0
    for i in items:
        if len(free_space) == 0:
            # print(free_space)
            # print(assignment)
            assignment[index] = index
            # buckets.append([i])
            free_space.append(1-i)

        elif free_space[-1] >= i:
            free_space[-1] -= i
            assignment.append(len(free_space) - 1)
            # assignment[index] =
        else:
            free_space.append(1 - i)
            assignment.append(len(free_space) - 1)
            # assignment[index] = len(free_space) - 1

        index += 1
        # print(f"added {i}")
        # print(f" Assignment: {assignment}")
        # print(f" Free Space: {free_space}")



if __name__ == "__main__":
    arr = [.5, .7, .5, .2, .4, .2, .5, .1, .6]

    next_fit(arr, [], [])
