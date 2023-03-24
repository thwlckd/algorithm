# 구현
# 치킨 배달

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
houses = []
chickens = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 1:
            houses.append((i, j))
        elif data[i][j] == 2:
            chickens.append((i, j))

# 치킨집 m개의 조합별 도시 치킨 거리중 최소값 구하기
candidates = list(combinations(chickens, m))
result = 1e9
for candidate in candidates:
    distance = 0
    for house in houses:
        temp = 1e9
        for row, col in candidate:
            temp = min(temp, abs(house[0] - row) + abs(house[1] - col))  # 현재 집과 현재 조합 중 가장 가까운 치킨집과의 거리 구하기
        distance += temp  # 현재 조합의 도시 치킨 거리
    result = min(result, distance)

print(result)

'''
입력 예시 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
출력 예시 1
5
입력 예시2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
출력 예시 2
10
'''