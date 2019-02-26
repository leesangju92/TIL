import sys
sys.stdin = open("5188.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]
    move = [0]*N*2
