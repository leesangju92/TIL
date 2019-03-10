arr = [7,8,10,10]


def making_permutation(k,n,visit, order = []):
    global arr, result
    if k == n:
        result += [order]
        return
    for i in range(n):
        if visit & (1 << i): continue
        if arr[i] in order:
            making_permutation(k+1, n, visit | (1 << i), order)
        else:
            making_permutation(k+1, n, visit | (1 << i), order + [arr[i]])



subset = []
order = []
result = []

for i in range(1<<4):
    order = []
    for j in range(4):
        if i & (1<<j):
            order += [arr[j]]
    subset += [[order]]

print(subset)

making_permutation(0,4,0)
print(result)
