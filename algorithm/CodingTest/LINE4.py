import sys
sys.stdin = open("LINE4.txt", "r")

N = int(input())
seats = list(map(int, input().split()))

first_idx, last_idx = 0, 0
first_check = False
max_distance = 0
for idx in range(N):
    if seats[idx] == 1:
        max_distance = max(max_distance, idx - last_idx)
        last_idx = idx
        if not first_check:
            first_idx = idx
            first_check = True

print(max(first_idx - 0, max_distance//2, N-1-last_idx))