import sys
from itertools import permutations
sys.stdin = open("LINE2.txt", "r")

num_list = list(map(int, input().split(" ")))
k = int(input()) - 1
num_list.sort()
per_list = [list(per) for per in permutations(num_list, len(num_list))]
answer = ""
for num in per_list[k]:
    answer += str(num)
print(answer)
