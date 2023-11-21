# 성적 평가
# 3 <= n <=100000  ->  O(nlogn)

n = int(input())
data = []
array = []
rank = []
sum = [0]*n
for i in range(3):
    data.append(list(map(int, input().split())))
for i in range(4):
    array.append([])
    rank.append([])
    for j in range(n):
        if i < 3:
            array[i].append([data[i][j], j])
            sum[j] += array[i][j][0]
        else:
            array[i].append([sum[j], j])
        rank[i].append(0)
    array[i].sort(key = lambda x: x[0], reverse=True)
array.append([])
cnt = 0
for i in range(4):
    for j in range(n):
        if j > 0:
            if array[i][j][0] == array[i][j-1][0]:
                cnt += 1
                rank[i][array[i][j][1]] = j - cnt
                continue
        rank[i][array[i][j][1]] = j
        cnt = 0

for i in range(4):
    for j in range(n):        
        print(rank[i][j] + 1, end=' ')
    print()
    