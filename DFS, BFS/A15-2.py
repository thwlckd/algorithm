from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    q = deque([start])
    distance = [-1] * (n + 1)
    distance[start] = 0

    while q:
        start = q.popleft()
        for now in graph[start]:
            if distance[now] == -1:
                distance[now] = distance[start] + 1
                q.append(now)

    return distance


distance = bfs(x)
flag = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)
