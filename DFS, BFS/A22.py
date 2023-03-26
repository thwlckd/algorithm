# BFS
# 블록 이동하기
# 로봇의 상태를 집합 자료형으로 관리 -> 큐에 들어간 좌표에 대해 반복 방문 x

from collections import deque

# 현 위치에서 이동 가능한 위치 반환 함수
def get_next_pos(pos, board):
    next_pos = []  # 이동 가능한 결과 리스트
    pos = list(pos)  # 집합 -> 리스트
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x:  # 로봇이 가로
        for i in [-1, 1]:  # 위/아래 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y:  # 로봇이 세로
        for i in [-1, 1]:  # 좌/우 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})      
    return next_pos  

def solution(board):
    # 맵 외곽에 벽(1)을 둘러 범위 판정 간소화
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    # BFS
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
print(solution(board))

'''
입력 샘플
5
0 0 0 1 1
0 0 0 1 0
0 1 0 1 1
1 1 0 0 1
0 0 0 0 0
출력 샘플
7
'''