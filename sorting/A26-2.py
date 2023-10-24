# 카드 정렬하기
# 2회차

import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

sum = 0
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    sum += a + b
    heapq.heappush(heap, a + b)

print(sum)
