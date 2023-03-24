# 그래프
# 최종 순위
# 위상 정렬
# 정해진 우선순위(순위 변동 팀)에 따라 전체 팀의 순위를 나열

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    indegree = [0] * (n + 1)  # 진입 차수
    graph = [[False] * (n + 1) for i in range(n+1)]  # 간선 정보 담기위한 인접 행렬
    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True  # 높은 순위에서 낮은 순위를 가르키도록 간선 설정(1등 팀: 진입차수 0)
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 순위 변경 -> 간선 방향 뒤집기 + 진입차수 재설정
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    certain = True  # 위상 정렬 결과가 하나인지 여부
    cycle = False
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:  # 큐 원소 2개 이상 -> 가능한 정렬 결과가 여러개
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:  # 새로 진입차수 0이된 노드 삽입
                    q.append(j)
    
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()

'''
입력 샘플
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
출력 샘플
5 3 2 4 1
2 3 1
IMPOSSIBLE
'''