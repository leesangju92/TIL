arr = [55, 7, 78, 12, 42]
N = len(arr)

for l in range(1,N-1):
    for i in range(N-l):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)