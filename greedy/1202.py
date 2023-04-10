# 보석 도둑

import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 보석, 가방
jewel = []
for _ in range(n):
    jewel.append(list(map(int, input().split())))  # 보석 무게, 가격
bags = []
for _ in range(k):
    bags.append(int(input()))  # 가방 최대 무게

jewel.sort()
bags.sort()

jewel_box = []
result = 0
for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(jewel_box, -jewel[0][1])  # 최대힙 사용
        heapq.heappop(jewel)
    if jewel_box:
        result -= heapq.heappop(jewel_box)

print(result)

'''
입력 샘플
3 2
1 65
5 23
2 99
10
2
출력 샘플
164
'''