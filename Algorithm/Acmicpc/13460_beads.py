import sys
sys.stdin = open("13460_beads.txt", "r")

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())



boards = [[Str for Str in input()] for _ in range(N)]


flip_count = 0
for dx, dy in dxy:





for bb in boards:
    print(bb)