# 구현
# 뱀

from collections import deque

def turn(head, c):
    if c == 'L':
        head = (head - 1) % 4
    else:
        head = (head + 1) % 4
    return head

n = int(input())  # NxN map
k = int(input())  # 사과 개수
data = [[0] * n for _ in range(n)]  # 0: 빈칸, 1: 사과, 2: 뱀

for i in range(k):
    a, b = map(int, input().split())  # (행, 열)
    data[a-1][b-1] = 1

l = int(input())  # 방향 변경 횟수
direction = []
for i in range(l):
    direction.append(tuple(input().split()))  # (초, 방향) L: 왼쪽 90도, D: 오른쪽 90도

# 동 남 서 북
head = 0  # 0, 1, 2, 3
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
count = 0  # 방향 전환 횟수
q = deque()  # 뱀의 현재 좌표 [꼬리, .. 몸통 .. , 머리]
x, y = 1, 1
q.append((x, y))  # 시작 좌표
while True:
    time += 1
    nx = x + dx[head]
    ny = y + dy[head]
    if nx > 0 and nx <= n and ny > 0 and ny <= n and data[nx-1][ny-1] != 2:
        if data[nx-1][ny-1] == 1:  # 사과 위치 방문
            data[nx-1][ny-1] = 2
        else:  # 빈칸 방문
            x, y = q.popleft()
            data[x-1][y-1] = 0
        q.append((nx, ny))
        data[nx-1][ny-1] = 2
    else:
        break
    x, y = nx, ny

    if count < l and time == int(direction[0][0]):
        c = direction.pop(0)[1]
        head = turn(head, c)
        count += 1

print(time)

'''
입력 예시 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
출력 예시 1
9
입력 예시 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
출력 예시 2
21
입력 예시 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
출력 예시 3
13
'''