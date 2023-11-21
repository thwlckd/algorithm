# 스타트와 링크

from itertools import combinations

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

idx = list(range(n))
result = 1e9
for team1 in combinations(idx, n//2):
    power1 = 0
    power2 = 0
    team2 = list(set(idx) - set(team1))
    for i, j in combinations(team1, 2):
        power1 += data[i][j] + data[j][i]
    for i, j in combinations(team2, 2):
        power2 += data[i][j] + data[j][i]
    result = min(result, abs(power1-power2))

print(result)
    
'''
입력 예제 1
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
출력 예제 1
0
입력 예제 2
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
출력 예제 2
1
'''