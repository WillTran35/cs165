from collections import deque

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

def merge(first, next):
    pass

def tim_sort(arr):
    runs = make_runs(arr)
    stack = deque()
    while len(runs) > 0:
        run = runs.pop(0)
        stack.append(run)
        height = len(stack)
        while True:
            if height >= 3 and len(stack[1]) > len(stack[3]):
                merge(stack[2], stack[3])
            elif height >= 2 and len(stack[1]) >= len(stack[2]):
                merge(stack[1], stack[2])
            elif height >= 3 and len(stack[1]) + len(stack[2]) >= len(stack[3]):
                merge(stack[1], stack[2])
            elif height >= 4 and len(stack[2]) + len(stack[3]) >= len(stack[4]):
                merge(stack[1], stack[2])
            else:
                break
    while len(stack) != 1:
        merge(stack[1], stack[2])


if __name__ == '__main__':
    x = [4,5,9,3,1,10]
    print(make_runs(x))

