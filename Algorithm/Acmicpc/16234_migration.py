import sys
sys.stdin = open("16234_migration.txt", "r")

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

result = 0
not_move = False
while not not_move:
    not_move = True
    visit = [[False for _ in range(N)] for _ in range(N)]
    for I in range(N):
        for J in range(N):
            if not visit[I][J]:
                countries_path = []
                countries_group = []
                countries_path.append((I, J))
                countries_group.append((I, J))
                countries_sum = countries[I][J]
                visit[I][J] = True
                while len(countries_path):
                    X, Y = countries_path.pop(0)
                    for dx, dy in dxy:
                        if 0 <= X + dx < N and 0 <= Y + dy < N and not visit[X+dx][Y+dy]:
                            if L <= abs(countries[X][Y] - countries[X+dx][Y+dy]) <= R:
                                visit[X+dx][Y+dy] = True
                                countries_path.append((X+dx, Y+dy))
                                countries_group.append((X+dx, Y+dy))
                                countries_sum += countries[X+dx][Y+dy]
                if len(countries_group) > 1:
                    not_move = False
                    for i, j in countries_group:
                        countries[i][j] = int(countries_sum / len(countries_group))
    if not not_move:
        result += 1

print(result)
