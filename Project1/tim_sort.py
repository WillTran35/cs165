import time
def make_runs(arr):
    result = []
    temp = []
    index = 0
    for i in arr:
        if len(temp) == 0:
            temp.append(index)
        elif i >= arr[temp[-1]]:
            temp.append(index)
        else:
            result.append(temp)
            temp = [index]
        index += 1

    if len(temp) != 0:
        result.append(temp)

    return result


def merge(first, second, result):
    first_len = len(first)
    second_len = len(second)
    pos1 = 0
    pos2 = 0
    start = first[0]
    sub_arr = []
    while not pos1 >= first_len and not pos2 >= second_len:
        # print(pos1, pos2)
        if result[first[pos1]] < result[second[pos2]]:
            sub_arr.append(result[first[pos1]])
            pos1 += 1
            start += 1
        elif result[first[pos1]] > result[second[pos2]]:
            sub_arr.append(result[second[pos2]])
            pos2 += 1
            start += 1
        else:
            sub_arr.append(result[first[pos1]])
            start += 1
            sub_arr.append(result[second[pos2]])
            start += 1
            pos1 += 1
            pos2 += 1

    if pos1 < first_len:
        # print(first[pos1:])
        for i in first[pos1:]:
            # print(i)
            sub_arr += [result[i]]
        # sub_arr += result[first[pos1:]]

    elif pos2 < second_len:
        for i in second[pos2:]:
            # print(i)
            sub_arr += [result[i]]
        # sub_arr += result[second[pos2:]]
    merged_indexes = first + second
    # print(sub_arr)
    count = 0
    for i in range(first[0], second[-1] + 1):
        result[i] = sub_arr[count]
        count += 1
    return merged_indexes


def tim_sort(arr):
    start = time.perf_counter_ns()
    runs = make_runs(arr)
    stack = []
    while len(runs) != 0:
        run = runs.pop(0)
        stack.append(run)
        height = len(stack)
        while True:
            if height >= 3 and len(stack[0]) > len(stack[2]):
                stack[1] = merge(stack[1], stack[2], arr)
                stack.pop(2)
            elif height >= 2 and len(stack[0]) >= len(stack[1]):
                stack[0] = merge(stack[0], stack[1], arr)
                stack.pop(1)
            elif height >= 3 and len(stack[0]) + len(stack[1]) >= len(stack[2]):
                stack[0] = merge(stack[0], stack[1], arr)
                stack.pop(1)
            elif height >= 4 and len(stack[1]) + len(stack[2]) >= len(stack[3]):
                stack[0] = merge(stack[0], stack[1], arr)
                stack.pop(1)
            # print(f"Stack: {stack}")
            break
    while len(stack) != 1:
        stack[0] = merge(stack[0], stack[1], arr)
        stack.pop(1)
    end = time.perf_counter_ns()
    return end-start


if __name__ == '__main__':
    x = [96, 38, 81, 57, 63, 21, 14, 13, 50, 74]
    print(x)
    print(make_runs(x))
    print(tim_sort(x))

