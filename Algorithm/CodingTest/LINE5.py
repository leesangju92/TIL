import sys
sys.stdin = open("LINE5.txt", "r")

from math import factorial

def PER_fomula(n, m):
    return int(factorial(n+m) / (factorial(n) * factorial(m)))

n, m = map(int, input().split())
cony_n, cony_m = map(int, input().split())

if 0 <= cony_n <= n and 0 <= cony_m <= m:
    print(cony_n + cony_m)
    print(PER_fomula(cony_n, cony_m))
else:
    print("fail")