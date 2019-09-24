import sys
sys.stdin = open("14500_tetromino.txt", "r")

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def three_blocks(y, x, score, dup, n=0):
    global max_score, game_board, dxy
    if n == 3:
        if score > max_score:
            max_score = score
        return
    for dx, dy in dxy:
        if (0 <= x+dx < M) and (0 <= y+dy < N) and (y+dy, x+dx) not in dup:
            three_blocks(y+dy, x+dx, score+(game_board[y+dy][x+dx]), dup+[(y+dy, x+dx)], n+1)

N, M = map(int, input().split())
game_board = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

for n in range(N):
    for m in range(M):
        three_blocks(n, m, game_board[n][m], [(n, m)])
        if 0 <= n-1 < N and 0 <= m+2 < M:
            SCORE = game_board[n][m] + game_board[n][m+1] + game_board[n][m+2] + game_board[n-1][m+1]
            if max_score < SCORE:
                max_score = SCORE
        if 0 <= n+1 < N and 0 <= m+2 < M:
            SCORE = game_board[n][m] + game_board[n][m+1] + game_board[n][m+2] + game_board[n+1][m+1]
            if max_score < SCORE:
                max_score = SCORE
        if 0 <= n+2 < N and 0 <= m-1 < M:
            SCORE = game_board[n][m] + game_board[n+1][m-1] + game_board[n+1][m] + game_board[n+2][m]
            if max_score < SCORE:
                max_score = SCORE
        if 0 <= n+2 < N and 0 <= m+1 < M:
            SCORE = game_board[n][m] + game_board[n+1][m+1] + game_board[n+1][m] + game_board[n+2][m]
            if max_score < SCORE:
                max_score = SCORE

print(max_score)