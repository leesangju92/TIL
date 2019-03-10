import sys
sys.stdin = open("chef.txt","r")

def making_set(k, n, start, ingre = []):
    global subset
    if k == n:
        subset += [ingre]
        return
    for i in range(start, N):
        making_set(k+1, n, i+1, ingre+[i] )

def synerge(subset, set_sum):
    global arr
    for I in range(len(subset)):
        for J in range(len(subset)):
            if I == J:
                continue
            set_sum += arr[subset[I]][subset[J]]
    return set_sum

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        arr += [list(map(int, input().split()))]
    subset = []
    making_set(0, N//2, 0)
    minimum = 100000000000

    for i in range(len(subset)//2):
        set_sum = 0
        another_sum = 0
        another_set = list(set(list(range(N))) - set(subset[i]))
        if minimum > abs(synerge(subset[i], set_sum) - synerge(another_set, another_sum)):
            minimum = abs(synerge(subset[i], set_sum) - synerge(another_set, another_sum))
    print(f"#{test_case} {minimum}")



