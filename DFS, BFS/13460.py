# 구슬 탈출 2
# BFS

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            red_x, red_y = i, j
        if graph[i][j] == 'B':
            blue_x, blue_y = i, j
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # visited[red_x][red_y][blue_x][blue_y]
visited[red_x][red_y][blue_x][blue_y] = True
q = deque()
q.append((red_x, red_y, blue_x, blue_y, 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy, count):
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    while q:
        red_x, red_y, blue_x, blue_y, distance = q.popleft()
        if distance > 10:  # 거리 10 초과시 skip
            continue
        for i in range(4):  # 4방향 탐색
            red_nx, red_ny, distance_red = move(red_x, red_y, dx[i], dy[i], 0)
            blue_nx, blue_ny, distance_blue = move(blue_x, blue_y, dx[i], dy[i], 0)
            if graph[blue_nx][blue_ny] == 'O':  # 파란공이 나온 경우 무시
                continue
            if graph[red_nx][red_ny] == 'O':  # 빨간공이 나온경우 성공
                return print(distance)
            # 두 구슬의 위치가 겹칠경우 구슬의 이동 거리에 따른 위치 조정
            if (red_nx, red_ny) == (blue_nx, blue_ny):
                if distance_red < distance_blue:
                    blue_nx -= dx[i]
                    blue_ny -= dy[i]
                else:
                    red_nx -= dx[i]
                    red_ny -= dy[i]
            if visited[red_nx][red_ny][blue_nx][blue_ny] == False:
                visited[red_nx][red_ny][blue_nx][blue_ny] = True
                q.append((red_nx, red_ny, blue_nx, blue_ny, distance+1))
    print(-1)  # 탈출 가능 경우 x
                
bfs()

'''
입력 예제
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
출력 예제
5

10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########
10

8 8
########
#BR.#.O#
###.#..#
#...#..#
#.###..#
#..#..##
##...#.#
########
-1
'''