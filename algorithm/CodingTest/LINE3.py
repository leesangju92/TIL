import sys
sys.stdin = open("LINE3.txt", "r")

from queue import PriorityQueue

N = int(input())
toilet_times = [list(map(int, input().split())) for _ in range(N)]
toilet_times.sort(key=lambda x: x[0])

answer = 0
pq = PriorityQueue()
while len(toilet_times):
    i, o = toilet_times.pop(0)
    if pq.qsize():
        fo = pq.get()
        if fo <= i:
            pq.put(o)
        else:
            pq.put(fo)
            pq.put(o)
    else:
        pq.put(o)
    answer = max(answer, pq.qsize())

print(answer)