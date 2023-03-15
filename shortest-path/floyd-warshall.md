## floyd-warshall
모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 알고리즘

## 구현
DP를 이용하여 방문하는 모든 노드에 대해 최단 거리 테이블을 갱신
* D<sub>ij</sub> = min(D<sub>ik</sub>, D<sub>ik</sub> + D<sub>kj</sub>)
```python
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
```


## floyd-warshall vs dijkstra
> 기본적으로 현재 방문하는 노드```graph[now]``` 기준으로 알고리즘 수행

|floyd-warshall|dijkstra|
|:--:|:--:|
|모든 지점에서 다른 모든 지점까지의 최단 경로|한 지점에서의 최단 경로|
|현재 노드를 거쳐가는 모든 경로 고려|방문하지 않은 노드 중 최단거리를 갖는 노드 방문|
|최단 거리 리스트 2차원|최단 거리 리스트 1차원|
|다이나믹 프로그래밍 기반(D<sub>ab</sub> = min(D<sub>ab</sub>, D<sub>ak</sub> + D<sub>kb</sub>)|그리디 기반|
|O(V<sup>3</sup>)|O(ElogV) or O(V<sup>2</sup>)|

