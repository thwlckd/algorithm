import copy

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
result = 0


def virus(data, x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
            continue
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            virus(data, nx, ny)


def dfs(count):
    if count == 3:
        temp = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(temp, i, j)

        global result
        safe_zone = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    safe_zone += 1
        result = max(result, safe_zone)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)
