import sys
sys.stdin = open("14503_robot.txt", "r")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d 0:북, 1:동, 2:남 3:서

rcds = [[(0, -1, 3), (1, 0, 2), (0, 1, 1), (-1, 0, 0)],
        [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)],
        [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)],
        [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)]]

ground = [list(map(int, input().split())) for _ in range(N)]

cleaned_area = 0
i = 3
while True:
    i += 1
    check = False

    if ground[r][c] == 0:
        cleaned_area += 1
        ground[r][c] = i

    for dr, dc, new_d in rcds[d]:
        if (0 <= r + dr < N) and (0 <= c + dc < M):
            if ground[r+dr][c+dc] == 0:
                r = r + dr
                c = c + dc
                d = new_d
                check = True
                break

    if not check:
        if d == 0:
            if ground[r+1][c] == 1:
                break
            r = r + 1
        elif d == 1:
            if ground[r][c-1] == 1:
                break
            c = c - 1
        elif d == 2:
            if ground[r-1][c] == 1:
                break
            r = r - 1
        elif d == 3:
            if ground[r][c+1] == 1:
                break
            c = c + 1

print(cleaned_area)