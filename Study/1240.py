import sys
sys.stdin = open("1240.txt", "r")

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    if N <= 5 or M <= 56:
        print(f"#{t} 0")
        continue
    password_codes = []
    for n in range(N):
        password_codes += [input()]
