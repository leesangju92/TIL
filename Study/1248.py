import sys
sys.stdin = open("1248.txt", "r")

T = int(input())
for test_case in range(2):
    V, E, target1, target2 = map(int, input().split())
    arr = list(map(int, input().split()))
    connection = []
    for v in range(V-1):
        connection += [[arr[2*v], arr[2*v+1]]]

