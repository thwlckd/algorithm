# 시험 감독

import math
import sys
input = sys.stdin.readline

n = int(input())  # 시험장 개수
candidates = list(map(int, input().split()))  # 응시자 수
main_supervisor, sub_supervisor = map(int, input().split())  # 총감독, 부감독 수

count = n
for i in range(len(candidates)):
    candidates[i] -= main_supervisor
    if candidates[i] > 0:
        temp = math.ceil(candidates[i] / sub_supervisor)
        count += temp

print(count)

'''
입력 예시
5
10 9 10 9 10
7 2
출력 예시
13
'''