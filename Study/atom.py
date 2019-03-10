import sys
sys.stdin = open("atom.txt","r")

dxy = [[1,0],[-1,0],[0,-1],[0,1]]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        X, Y, D, K = map(int, input().split())
        arr += [[[Y, X], D, K]]
    for a in range(len(arr)):
        for b in range(len(arr)):





    print(arr)

    # print(f"#{test_case} {total_energy}")
