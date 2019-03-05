import sys
sys.stdin = open("fire.txt","r")

T = int(input())
for test_case in range(1, T+1):
    W, H = map(int, input().split())
    arr = []
    for h in range(H):
        arr += [input()]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    location = [[] for _ in range(3)]
    # for i in range(H):
        # for j in range[]
        