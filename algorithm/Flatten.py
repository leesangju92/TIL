import sys
sys.stdin = open("input.txt", "r")

for i in range(10):
    Dump = int(input())
    arr = list(map(int, input().split()))
    min = arr[0]
    max = 0
    box_dict = {i: 0 for i in range(1, 101)}
    for floor in arr:
        box_dict[floor] += 1
        if floor > max:
            max = floor
        elif floor < min:
            min = floor
    for d in range(Dump):
        box_dict[max] -= 1
        box_dict[max-1] += 1
        box_dict[min] -= 1
        box_dict[min+1] += 1
        if box_dict[max] == 0:
            max -= 1
        if box_dict[min] == 0:
            min += 1
    print(f"#{i+1} {max - min}")


    #
    #
    # i = 0
    # for floor in arr:
    #     if arr[i] == max:
    #          max_index += [i]
    #     elif arr[i] == min:
    #         min_index += [i]
    #     i += 1
    #
    # print(max_index, min_index, max, min)
