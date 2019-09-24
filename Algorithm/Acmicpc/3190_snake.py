import sys
sys.stdin = open("3190_snake.txt", "r")

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
# -1는 빈칸 0,1,2,3 방향, 4는 사과
board = [[-1 for _ in range(N)] for _ in range(N)]
board[0][0] = 0

for k in range(int(input())):
    coor_y, coor_x = map(int, input().split())
    board[coor_y-1][coor_x-1] = 4

direction_changes = []
for l in range(int(input())):
    time, D = input().split()
    direction_changes.append((int(time), D))

# L 또는 D, 왼쪽, 오른쪽 90도 회전
# 뱀은 처음에 오른쪽을 향하며, 맨왼쪽 맨위에서 시작, 길이는 1

t = 0
direction = 0
head = (0, 0)
tail = (0, 0)

while True:
    t += 1
    if len(direction_changes) and direction_changes[0][0] == t-1:
        direction_change = direction_changes.pop(0)
        if direction_change[1] == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

    new_head = (head[0] + dxy[direction][0], head[1] + dxy[direction][1])

    if (0 <= new_head[0] < N) and (0 <= new_head[1] < N):
        # 사과일 경우?
        if board[new_head[0]][new_head[1]] == 4:
            board[head[0]][head[1]] = direction
            head = new_head
        # 뱀일 경우?
        elif board[new_head[0]][new_head[1]] >= 0:
            break
        else:
            board[head[0]][head[1]] = direction
            prev_direction = board[tail[0]][tail[1]]
            new_tail = (tail[0] + dxy[prev_direction][0], tail[1] + dxy[prev_direction][1])
            board[tail[0]][tail[1]] = -1
            tail = new_tail
            head = new_head
    else:
        break
print(t)

