import sys
sys.stdin = open("input1.txt", "r")  #해당 파일로부터 input 받음
sys.stdout = open("output1.txt", "w") #해당 파일로 출력하여 저장
# \\70.12.107.120 공유폴더


T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(N)
    print(arr)

T = int(input())   # 표형태로 정보 입력
for test_case in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    print(N)
    print(arr)

T = int(input())
for test_case in range(T):
    N, arr = input(),split()
    N = int(N)
    print(N, arr)

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        tmp = input()
        for j in range(N):
            arr[i][j] = int(tmp[j])
        print(arr[i])
