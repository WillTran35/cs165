import time


def make_runs(arr):
    result = []
    temp = []
    index = 0
    n = len(arr)

    while index < n:
        temp = [index]
        index += 1

        # Handle increasing run
        while index < n and arr[index] >= arr[index - 1]:
            temp.append(index)
            index += 1

        # If run is too short or we have a decreasing run
        if index < n and (len(temp) < 2 or arr[index] < arr[index - 1]):
            # Extend for minimum run size or handle decreasing run
            while index < n and (len(temp) < 2 or (arr[index] < arr[index - 1] and index < n)):
                temp.append(index)
                index += 1
            # Reverse decreasing run
            if len(temp) > 1 and arr[temp[-1]] < arr[temp[0]]:
                temp.reverse()

        result.append(temp)

    return result


def merge(first, second, result):
    first_len = len(first)
    second_len = len(second)
    pos1 = 0
    pos2 = 0
    sub_arr = []

    while pos1 < first_len and pos2 < second_len:
        if result[first[pos1]] <= result[second[pos2]]:
            sub_arr.append(result[first[pos1]])
            pos1 += 1
        else:
            sub_arr.append(result[second[pos2]])
            pos2 += 1

    # Append remaining elements
    sub_arr.extend(result[i] for i in first[pos1:])
    sub_arr.extend(result[i] for i in second[pos2:])

    # Update result array
    merged_indexes = first + second
    for i, val in zip(range(first[0], second[-1] + 1), sub_arr):
        result[i] = val

    return merged_indexes


def tim_sort(arr):
    start = time.perf_counter_ns()
    runs = make_runs(arr.copy())  # Work on a copy to preserve input
    stack = []

    for run in runs:
        stack.append(run)

        # Maintain TimSort invariants
        while len(stack) >= 2:
            # TimSort merge conditions
            # A > B + C and B > C
            if (len(stack) >= 3 and len(stack[-3]) <= len(stack[-2]) + len(stack[-1])) or \
                    (len(stack) >= 2 and len(stack[-2]) <= len(stack[-1])):
                # Merge smaller of stack[-2] with stack[-1] or stack[-3] with stack[-2]
                if len(stack) >= 3 and len(stack[-3]) < len(stack[-1]):
                    stack[-3] = merge(stack[-3], stack[-2], arr)
                    stack.pop(-2)
                else:
                    stack[-2] = merge(stack[-2], stack[-1], arr)
                    stack.pop(-1)
            else:
                break

    # Final merges
    while len(stack) > 1:
        stack[-2] = merge(stack[-2], stack[-1], arr)
        stack.pop(-1)

    end = time.perf_counter_ns()
    return arr, end - start


if __name__ == '__main__':
    x = [96, 38, 81, 57, 63, 21, 14, 13, 50, 74]
    print("Input:", x)
    print("Runs:", make_runs(x))
    sorted_arr, time_taken = tim_sort(x)
    print("Sorted:", sorted_arr)
    print("Time (ns):", time_taken)