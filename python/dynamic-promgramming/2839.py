# 설탕배달
# ai = min(ai, ai-k + 1) / ai = inf

n = int(input())
INF = n+1
d = [INF] * (n+1)
d[0] = 0
array = [3, 5]
for i in range(len(array)):
    for j in range(3, n+1):
        if d[j-array[i]] != INF:
            d[j] = min(d[j], d[j-array[i]] + 1)
if d[n] != INF:
    print(d[n])
else:
    print(-1)
