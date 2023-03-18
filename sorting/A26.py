# 정렬
# 카드 정렬하기

import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
sum = 0
while len(heap) > 1:    
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    sum += a+b
    heapq.heappush(heap, a+b)
print(sum)

'''
입력 샘플
4
10
20
40
50
출력 샘플
220
'''