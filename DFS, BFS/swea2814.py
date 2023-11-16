# 최장 경로


def dfs(index, cost):
    global result

    visited[index] = True

    result = max(result, cost)

    for i in graph[index]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, cost + 1)
            visited[i] = False

    visited[index] = False


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = 0
    for i in range(1, n + 1):
        dfs(i, 1)

    print(f"#{test_case} {result}")
