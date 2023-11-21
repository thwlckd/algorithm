# 강의실 배정

import heapq
import sys

input = sys.stdin.readline

n = int(input())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, input().split())))

lecture.sort()

q = []
heapq.heappush(q, lecture[0][0])
for time in lecture:
    if time[0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, time[1])
    else:
        heapq.heappush(q, time[1])

print(len(q))
