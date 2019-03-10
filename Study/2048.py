import sys
sys.stdin = open("2048.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N, key = map(str, input().split())
    N = int(N)
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]

    if key == "up":
        for i in range(N):
            for j in range(N):
                if arr[j][i] == 0:
                    for k in range(j+1,N):
                        if arr[k][i] != 0:
                            arr[j][i] = arr[k][i]
                            arr[k][i] = 0
                            break

                for l in range(j+1, N):
                    if arr[l][i] != 0 and arr[l][i] != arr[j][i]:
                        break
                    elif arr[l][i] != 0 and arr[l][i] == arr[j][i]:
                        arr[j][i] = arr[j][i] + arr[l][i]
                        arr[l][i] = 0
                        break

    if key == "left":
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    for k in range(j+1,N):
                        if arr[i][k] != 0:
                            arr[i][j] = arr[i][k]
                            arr[i][k] = 0
                            break

                for l in range(j+1, N):
                    if arr[i][l] != 0 and arr[i][l] != arr[i][j]:
                        break
                    elif arr[i][l] != 0 and arr[i][l] == arr[i][j]:
                        arr[i][j] = arr[i][j] + arr[i][l]
                        arr[i][l] = 0
                        break

    if key == "down":
        for i in range(N):
            for j in range(N-1, -1, -1):
                if arr[j][i] == 0:
                    for k in range(j-1,-1,-1):
                        if arr[k][i] != 0:
                            arr[j][i] = arr[k][i]
                            arr[k][i] = 0
                            break
                for l in range(j-1, -1, -1):
                    if arr[l][i] != 0 and arr[l][i] != arr[j][i]:
                        break
                    elif arr[l][i] != 0 and arr[l][i] == arr[j][i]:
                        arr[j][i] = arr[j][i] + arr[l][i]
                        arr[l][i] = 0
                        break
    if key == "right":
        for i in range(N):
            for j in range(N-1, -1, -1):
                if arr[i][j] == 0:
                    for k in range(j-1,-1,-1):
                        if arr[i][k] != 0:
                            arr[i][j] = arr[i][k]
                            arr[i][k] = 0
                            break
                for L in range(j-1, -1, -1):
                    if arr[i][L] != 0 and arr[i][L] != arr[i][j]:
                        break
                    elif arr[i][L] != 0 and arr[i][L] == arr[i][j]:
                        arr[i][j] = arr[i][j] + arr[i][L]
                        arr[i][L] = 0
                        break

    print("#{}".format(test_case))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
