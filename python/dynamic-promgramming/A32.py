# 다이나믹 프로그래밍
# 정수 삼각형

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))    

for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0:
            left_up = 0
        else:
            left_up = data[i-1][j-1]
        if j == i:
            right_up = 0
        else:
            right_up = data[i-1][j]
        data[i][j] = data[i][j] + max(left_up, right_up)

result = max(data[n-1])
print(result)

'''
입력 샘플
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
출력 샘플
30
'''