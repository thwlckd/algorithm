# 숨바꼭질 3

from collections import deque

n, k = map(int, input().split())
INF = int(1e9)
visited = [0] * 100001
q = deque()
deque.append(q, n)

while q:
    i = q.popleft()
    if i == k:
        print(visited[i])
        break

    for next_i in [i - 1, i + 1, i * 2]:
        if 0 <= next_i <= 100000 and visited[next_i] == 0:
            if next_i == i * 2 and next_i != 0:
                visited[next_i] = visited[i]
                q.appendleft(next_i)
            else:
                visited[next_i] = visited[i] + 1
                q.append(next_i)
