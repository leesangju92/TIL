k = 4
arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0]*(k+1)

for val in arr:
    cnt[val] += 1

print(cnt)

answer = []
for i in range(len(cnt)):
    if cnt[i] != 0:
        for l in range(cnt[i]):
            answer += [i]

print(answer)

answer2 = []
for idx in range(1, len(cnt)):
    cnt[idx] = cnt[idx-1] + cnt[idx]

print(cnt)
