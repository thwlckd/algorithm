# 구현
# 자물쇠와 열쇠
# 2020 카카오 신입 공채 기출

import copy

def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    expaned = [[0]*3*n for _ in range(3*n)]  # 자물쇠 확장
    for i in range(n):
        for j in range(n):
            expaned[n+i][n+j] = lock[i][j]
    for i in range(4):
        key = turn(key)
        # 열쇠 이동
        for x in range(2*n):
            for y in range(2*n):
                lock = copy.deepcopy(expaned)
                # 자물쇠에 열쇠 끼우기
                for j in range(m):
                    for k in range(m):
                        lock[x+j][y+k] += key[j][k]
                answer = check(lock)
                if answer == True:
                    return answer
    return answer

def turn(key):  # 오른쪽 90도
    n = len(key)
    new_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[j][n-i-1] = key[i][j]
    return new_key

def check(lock):
    n = len(lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if lock[i][j] != 1:
                return False
    return True