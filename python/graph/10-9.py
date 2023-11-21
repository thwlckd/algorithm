# 그래프 이론
# 위상 정렬(Topology Sort)

from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)  # 진입차수
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)
for i in range(1, n + 1):
    row = list(map(int, input().split()))  # 시간(비용), now, (b, c, ..), -1
    time[i] = row[0]
    for j in row[1:-1]:
        indegree[i] += 1
        graph[j].append(i)  # b, c, d -> now

def tolpoloy_sort():
    q = deque()
    result = copy.deepcopy(time)  # 리스트의 값을 복제

    # 진입차수 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            # 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우 선수강 강의 존재 / 갱신
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 진입차수가 0이 된 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])

tolpoloy_sort()

'''
입력 샘플
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
출력 샘플
'''
