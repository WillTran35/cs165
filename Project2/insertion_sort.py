import time

def getNums(runs, arr):
    result = []
    for i in runs:
        result.append(arr[i])
    return insertion_sort(result)
def insertion_sort(arr):
    start = time.perf_counter_ns()
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j -1]
            j -= 1
        arr[j] = temp
    end = time.perf_counter_ns()
    return arr
def make_runs(arr):
    result = []
    temp = []
    dec = None
    index = 0
    for i in arr:
        if len(temp) == 0:
            temp.append(index)
        elif i >= arr[temp[-1]] and (dec is None or dec is False):
            dec = False
            # print(f"dec is false {dec}")
            temp.append(index)
        elif i < arr[temp[-1]] and (dec is None or dec is True):
            dec = True
            # print(f"dec is true {dec}")
            temp.append(index)
        elif i < arr[temp[-1]] and (dec is False):
            result.append(temp)
            temp = [index]
            # print("adding ")
            dec = None
        elif i >= arr[temp[-1]] and (dec is True):
            # print(f"printing reverse {temp}")
            result.append(list(reversed(temp)))
            temp = [index]
            # print("adding reverse")
            dec = None
        index += 1

    if len(temp) != 0:
        if dec is True:
            result.append(list(reversed(temp)))
        else:
            result.append(temp)

    return result


def merge(first, second, result):
    first_len = len(first)
    second_len = len(second)
    pos1 = 0
    pos2 = 0
    start = first[0]
    sub_arr = []
    res = []
    print(f'first: {first} second: {second} result: {result}')
    while pos1 < first_len and pos2 < second_len:
        # print(pos1, pos2)
        if result[first[pos1]] < result[second[pos2]]:
            sub_arr.append(result[first[pos1]])
            res.append(first[pos1])
            pos1 += 1
            start += 1
            print(f"appended here {sub_arr}")
        elif result[first[pos1]] > result[second[pos2]]:
            sub_arr.append(result[second[pos2]])
            res.append(second[pos2])
            pos2 += 1
            start += 1
            print(f"appended here2 {sub_arr}")
        else:
            sub_arr.append(result[first[pos1]])
            start += 1
            sub_arr.append(result[second[pos2]])
            res.append(first[pos1])
            res.append(second[pos2])
            start += 1
            pos1 += 1
            pos2 += 1

            print(f"appended here3 {sub_arr}")

    if pos1 < first_len:
        # print(first[pos1:])
        for i in first[pos1:]:
            # print(i)
            sub_arr += [result[i]]
            res.append(i)
        print(f"appended here4 {sub_arr}")
        # sub_arr += result[first[pos1:]]

    elif pos2 < second_len:
        # count = pos2
        for i in second[pos2:]:
            # print(i)
            sub_arr += [result[i]]
            res.append(i)
            # count += 1
        print(f"appended here5 {sub_arr}")
        # sub_arr += result[second[pos2:]]
    # merged_indexes = first + second
    # # print(sub_arr)
    count = 0
    merged_indexes = res
    print(f"my merged indexes {merged_indexes}")
    minimum = min(merged_indexes)

    # for i in range(len(merged_indexes)):
    #     result[minimum] = sub_arr[i]
    #     minimum += 1
    # print(f"result: {result}")
    # return merged_indexes

    # for idx in merged_indexes:
    #     result[idx] = sub_arr[count]
    #     count += 1
    print(f"merged indexes : {merged_indexes}")
    return merged_indexes, sub_arr


def tim_sort(arr):
    start = time.perf_counter_ns()
    runs = make_runs(arr)
    stack = []

    while len(runs) != 0:
        run = runs.pop(0)
        stack.append(run)
        height = len(stack)
        _ = None
        while True:
            if height >= 3 and len(stack[0]) > len(stack[2]):
                stack[1],_ = merge(stack[1], stack[2], arr)
                stack.pop(2)
            elif height >= 2 and len(stack[0]) >= len(stack[1]):
                stack[0],_ = merge(stack[0], stack[1], arr)
                stack.pop(1)
            elif height >= 3 and len(stack[0]) + len(stack[1]) >= len(stack[2]):
                stack[0],_ = merge(stack[0], stack[1], arr)
                stack.pop(1)
            elif height >= 4 and len(stack[1]) + len(stack[2]) >= len(stack[3]):
                stack[0],_ = merge(stack[0], stack[1], arr)
                stack.pop(1)
            # print(f"Stack: {stack}")
            break
    while len(stack) != 1:
        stack[0],_ = merge(stack[0], stack[1], arr)
        print("sortingi n here")
        stack.pop(1)
    end = time.perf_counter_ns()
    return _


if __name__ == '__main__':
    x = [0.54, 0.67, 0.46, 0.57, 0.06, 0.23, 0.83, 0.64, 0.47, 0.03, 0.53, 0.74, 0.36, 0.24, 0.07, 0.25, 0.05, 0.63, 0.43, 0.04]
    print(x)
    print(make_runs(x))
    print(tim_sort(x))

