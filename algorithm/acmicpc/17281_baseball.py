import sys
sys.stdin = open("17281_baseball.txt", "r")


def make_order(n=0, k=0, LIST = []):
    global order_list
    if n == 8:
        LIST.insert(3, 0)
        order_list.append(LIST)
        return
    for i in range(1, 9):
        if k & (1 << i):
            continue
        else:
            make_order(n + 1, k|(1<<i), LIST + [i])

order_list = []
hitter_results = []
N = int(input())
for n in range(N):
    hitter_results.append(list(map(int, input().split())))

# 순서 리스트 만들기
make_order()

# 1:안타, 2:2투타, 3:3루타, 4:홈런, 0:아웃

max_score = 0

for players in order_list:
    score = 0
    player_idx = 0
    round = 0
    while round < N:
        bases_1, bases_2, bases_3 = False, False, False
        OUT = 0
        while OUT < 3:
            hit = hitter_results[round][players[player_idx]]
            if hit == 1:
                score += bases_3
                bases_1, bases_2, bases_3 = True, bases_1, bases_2

            elif hit == 2:
                score += bases_3+bases_2
                bases_1, bases_2, bases_3 = False, True, bases_1

            elif hit == 3:
                score += bases_1 + bases_2 + bases_3
                bases_1, bases_2, bases_3 = False, False, True

            elif hit == 4:
                score += bases_1 + bases_2+bases_3 + 1
                bases_1 = bases_2 = bases_3 = False
            else:
                OUT += 1
            player_idx = (player_idx + 1) % 9
        round += 1
    if score > max_score:
        max_score = score

print(max_score)