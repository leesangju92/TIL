def three(k, n, N, visit):
    global result
    if k == n:
        case = []
        for number in order:
            case += [arr[number]]
        if case not in result:
            result += [case[:]]
        return
    for i in range(N):
        if visit&(1<<i):continue
        order[k] = i
        if k > 0 and order[k] < order[k-1] : continue
        three(k+1, n, N, visit|(1<<i))


arr = [5,6,7,8,9]

n = 3
N = 5
result = []
order = [0]*n

three(0,n,N,0)

print(result)