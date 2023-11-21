# DFS/BFS -> 조합 라이브러리 사용으로 대체
# 감시 피하기

from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []
for i in range(n):
    board.append(input().split())
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    if direction == 0:  # 왼쪽 감시
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:  # 오른쪽 감시
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:  # 위쪽 감시
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:  # 아래쪽 감시
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후, 시야에 학생이 잡히는지 검사
def process():  
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False
# 빈 공간에서 3곳을 뽑아 장애물 설치
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    # 설치한 장애물 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")

'''
입력 샘플 1
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
출력 샘플 1
YES
입력 샘플 2
4
S S S T
X X X X
X X X X
T T T X
출력 샘플 2
NO
'''