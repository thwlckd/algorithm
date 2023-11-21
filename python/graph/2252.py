# 줄 세우기
# 위상 정렬

import sys
from collections import deque

input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
indegree = [0] * (v + 1)
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
# 진입차수 0인 노드 큐에 삽입
for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    print(now, end=' ')
    # 새로 진입차수가 0이된 노드 큐에 삽입
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

'''
입력 샘플
3 2
1 3
2 3
출력 샘플
1 2 3
'''