def make_runs(arr):
    result = []
    temp = []
    for i in arr:
        if len(temp) == 0:
            temp.append(i)
        elif i >= temp[-1]:
            temp.append(i)
        else:
            result.append(temp)
            temp = [i]

    if len(temp) != 0:
        result.append(temp)

    return result

def merge(first, second):
    first_len = len(first)
    second_len = len(second)
    pos1 = 0
    pos2 = 0
    result = []
    while not pos1 >= first_len and not pos2 >= second_len:
        # print(pos1, pos2)
        if first[pos1] < second[pos2]:
            result.append(first[pos1])
            pos1 += 1
        elif first[pos1] > second[pos2]:
            result.append(second[pos2])
            pos2 += 1
        else:
            result.append(first[pos1])
            result.append(second[pos2])
            pos1 += 1
            pos2 += 1

    if pos1 < first_len:
        result += first[pos1:]

    elif pos2 < second_len:
        result += second[pos2:]

    return result


def tim_sort(arr):
    runs = make_runs(arr)
    stack = []
    while len(runs) != 0:
        run = runs.pop(0)
        stack.append(run)
        height = len(stack)
        print(f"this is : {len(runs)}" )
        while True:
            if height >= 3 and len(stack[0]) > len(stack[2]):
                stack[1] = merge(stack[1], stack[2])
                stack.pop(2)
            elif height >= 2 and len(stack[0]) >= len(stack[1]):
                stack[0] = merge(stack[0], stack[1])
                stack.pop(1)
            elif height >= 3 and len(stack[0]) + len(stack[1]) >= len(stack[2]):
                stack[0] = merge(stack[0], stack[1])
                stack.pop(1)
            elif height >= 4 and len(stack[1]) + len(stack[2]) >= len(stack[3]):
                stack[0] = merge(stack[0], stack[1])
                stack.pop(1)

            print(f"stack: {stack}")
            break
    while len(stack) != 1:
        stack[1] = merge(stack[1], stack[2])
        stack.pop(2)
    return stack[0]


if __name__ == '__main__':
    x = [4,5,9,3,1,10]
    # print(make_runs(x))
    # x = [4,5,9]
    # y = [1,10]
    # print(merge(x,y))

    print(tim_sort(x))

