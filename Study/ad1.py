import sys
sys.stdin = open("ad1.txt", "r")


def find_route(A, B, D):
    global count, arr
    if A == (N -1) and B == (N -1):
        if D == "세로" or D == "가로":
            count += 1
            return
    # 세로일때
    if D == "세로":
        if A + 1 < N:
            if B + 1 < N:
                if arr[A+1][B+1] == 0 and arr[A][B+1] == 0 and arr[A+1][B] == 0:
                    find_route(A+1, B+1, "대각선")
                    find_route(A + 1, B, "세로")
                elif arr[A+1][B] == 0:
                    find_route(A + 1, B, "세로")
            else:
                if arr[A+1][B] == 0:
                    find_route(A + 1, B, "세로")

    # 가로일때
    elif D == "가로":
        if B + 1 < N:
            if A + 1 < N:
                if arr[A+1][B+1] == 0 and arr[A][B+1] == 0 and arr[A+1][B] == 0:
                    find_route(A+1, B+1, "대각선")
                    find_route(A, B+1, "가로")
                elif arr[A][B+1] == 0:
                    find_route(A, B+1, "가로")
            else:
                if arr[A][B+1] == 0:
                    find_route(A, B+1, "가로")


    #  대각선일때
    elif D == "대각선":
        if (A+1) < N and (B+1) < N:
            if arr[A+1][B+1] == 0 and arr[A][B+1] == 0 and arr[A+1][B] == 0:
                find_route(A + 1, B + 1, "대각선")
                find_route(A, B + 1, "가로")
                find_route(A + 1, B, "세로")
            elif arr[A][B+1] == 0 and arr[A+1][B] == 0:
                find_route(A, B + 1, "가로")
                find_route(A + 1, B, "세로")
            elif arr[A][B+1] == 0:
                find_route(A, B + 1, "가로")
            elif arr[A+1][B] == 0:
                find_route(A + 1, B, "세로")
        elif (A+1) < N:
            if arr[A+1][B] == 0:
                find_route(A+1, B, "세로")
        elif (B+1) < N:
            if arr[A][B+1] == 0:
                find_route(A, B+1, "가로")

N = int(input())
arr = []
for n in range(N):
    arr += [list(map(int, input().split()))]

count = 0
if arr[1][0] == 0:
    find_route(1,0,"세로")
if arr[0][1] == 0:
    find_route(0,1,"가로")

print(count)
