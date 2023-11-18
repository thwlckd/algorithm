# 0/1 Knapsack
# 백트래킹 시간초과 -> dp


def dfs(depth, volume, value):
    global max_value

    if volume > K:
        return

    if max_value < value:
        max_value = value

    for i in range(depth, N):
        visited[i] = True
        dfs(i + 1, volume + data[i][0], value + data[i][1])
        visited[i] = False


T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    visited = [False] * N
    for i in range(N):
        max_value = 0
        dfs(i, 0, 0)
        result = max(result, max_value)

    print(f"#{test_case} {result}")
