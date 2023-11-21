# 최단 경로
# 다익스트라 ver.1
# O(V^2) / V: vertex -> V < 10000

import sys
input = sys.stdin.readline  # input()을 더 빠르게 동작: 입력 데이터 많을 경우 사용
INF = int(1e9)

n, m = map(int, input().split())  # 노드, 간선
start = int(input())
graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n + 1)  # 방문 테이블
distance = [INF] * (n + 1)  # 최단 거리 테이블

for _ in range(m):
    a, b, c = map(int, input().split())  # a노드에서 b노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
0
2
3
1
2
4

출력예시
0
2
3
1
2
4
'''
