import sys
sys.stdin = open("fire.txt","r")

T = int(input())
for test_case in range(1, T+1):
    W, H = map(int, input().split())
    arr = []
    for h in range(H):
        words = input()
        arr += [list(words)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    location = [[] for _ in range(3)]
    for number in [0, H-1]:
        for w in range(W):
            if arr[number][w] == ".":
                for delta in dxy:
                    if number+delta[0] < H and number+delta[0] >= 0 and w+delta[1] < W and w+delta[1] >= 0:
                        if arr[number+delta[0]][w+delta[1]] in [".", "@"]:
                            location[0] = [number, w]
                            break
    if len(location[0]) == 0:
        for number in [0, W - 1]:
            for h in range(H):
                if arr[h][number] == ".":
                    for delta in dxy:
                        if number + delta[0] < W and number + delta[0] >= 0 and h + delta[1] < H and h + delta[1] >= 0:
                            if arr[h + delta[1]][number + delta[0]] in [".", "@"]:
                                location[0] = [h, number]
                                break
    if len(location[0]) == 0:
        print("IMPOSSIBLE")
    else:
        visit = [[location[0][0], location[0][1]]]
        course = [[location[0][0], location[0][1]]]
        a = 0
        count = 1
        while a == 0:
            count += 1
            new_course = []
            for start in course:
                if a == 1 or a == 2:
                    break
                for delta in dxy:
                    if start[0] + delta[0] < H and start[0] + delta[0] >= 0 and start[1] + delta[1] < W and start[1] + delta[1] >= 0:
                        if [start[0]+delta[0],start[1]+delta[1]] not in visit:
                            if arr[start[0]+delta[0]][start[1]+delta[1]] == "*":
                                a = 1
                                break
                            elif arr[start[0]+delta[0]][start[1]+delta[1]] == "@":
                                a = 2
                                break
                            elif arr[start[0]+delta[0]][start[1]+delta[1]] == ".":
                                new_course += [[start[0]+delta[0], start[1]+delta[1]]]
                                visit += [[start[0]+delta[0], start[1]+delta[1]]]
            course = new_course[:]
        if a == 1:
            print("IMPOSSIBLE")
        elif a == 2:
            print(count)




