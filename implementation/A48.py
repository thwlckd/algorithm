# 시뮬레이션
# 어른 상어

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

array = []  # 상어의 위치
for i in range(n):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))  # 상어의 현재 방향

smell = [[[0, 0]] * n for _ in range(n)]  # [상어, 냄새 남은 시간]

priorities = [[] for _ in range(m)]  # 회전 우선순위
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 현재 상어 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

def move():
    new_array = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if array[x][y] != 0:
                direction = directions[array[x][y] - 1]  # 해당 위치 상어의 방향
                found = False  # 주변에 냄새로 인해 이동할 수 없는지 판별
                # 상하좌우 중 이동할 곳 판별
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:  # 냄새 x
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]  # 이동한 방향이 바라보는 방향이 됨
                            # 상어 이동
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:  # 상어가 있다면 번호가 작은 상어
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]: # 자신의 냄새가 있는 곳으로 이동, 방향 변경
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell()  # 냄새 업데이트
    new_array = move()  # 상어 이동
    array = new_array
    time += 1

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break

'''
입력 예시
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
출력 예시
14
'''