### dijkstra
특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
> 음의 간선이 없을 때 동작

### 동작
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택(그리디)
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3-4 반복

### 구현
1. ver.1: get_smallest_node() 함수
   * 최단 거리가 가장 짧은 노드를 선택하는 과정
   * O(V<sup>2</sup>)
2. ver.2: 우선순위 큐(heapq) 사용
   * ver.1 일련의 과정을 우선순위 큐로 대체
   * ```heapq.heappush(q, (cost, i[0]))```
   * ```dist, now = heapq.heappop(q)```
   * O(ElogV)
```python
# ver.2
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 이미 처리된 적이 있는 노드 무시
            continue
        # 현재 노드의 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
```
