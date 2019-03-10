import sys
sys.stdin = open("switch.txt", "r")

def range_check(x,y):
    if 0 <= x < N and 0<= y < N:
        return True
    else:
        False

N = int(input())
arr = list(map(int, input().split()))
students = int(input())
changes = []
for student in range(students):
    changes += [list(map(int, input().split()))]

for change in changes:
    if change[0] == 1:
        for idx in range(change[1]-1, N):
            if (idx+1) % change[1] == 0:
                arr[idx] = abs(arr[idx]-1)
    else:
        arr[(change[1]-1)] = abs(arr[(change[1]-1)]-1)
        i = 0
        while arr[(change[1]-1)-i] == arr[(change[1]-1)+i]:
            arr[(change[1]-1) - i] = abs(arr[(change[1]-1)-i]-1)
            arr[(change[1]-1) + i] = abs(arr[(change[1]-1)+i]-1)
            i += 1
            if not range_check((change[1]-1)-i, (change[1]-1)+i):
                break
for x in range(len(arr)):
    if (x+1) % 20 == 0:
        print(arr[x])
    else:
        print(arr[x], end=" ")


