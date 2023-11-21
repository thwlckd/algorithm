# 다이나믹 프로그램
# 금광
# dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    cnt = 0
    for j in range(1, n + 1):
        for k in range(1, m + 1):
            graph[j][k] = data[cnt]
            cnt += 1
    for k in range(2, m + 1):
        for j in range(1, n + 1):
            if j == 1:
                left_up = 0
            else:
                left_up = graph[j-1][k-1]
            if j == n:
                left_down = 0
            else:
                left_down = graph[j+1][k-1]
            left = graph[j][k-1]
            graph[j][k] = graph[j][k] + max(left_up, graph[j][k-1], left_down)
    result = 0
    for j in range(1, n + 1):
        result = max(result, graph[j][m])
    print(result)

'''
입력 샘플
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
출력 샘플
19
16
'''
