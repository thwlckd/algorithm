# Flatten

import heapq

T = 10

for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    max_heap = []
    min_heap = []
    for now in arr:
        heapq.heappush(max_heap, -now)
        heapq.heappush(min_heap, now)

    diff = -(max_heap[0]) - min_heap[0]
    for _ in range(dump):
        high = -heapq.heappop(max_heap)
        low = heapq.heappop(min_heap)
        if diff < high - low:
            break
        heapq.heappush(max_heap, -(high - 1))
        heapq.heappush(min_heap, low + 1)
        diff = high - low

    high = -heapq.heappop(max_heap)
    low = heapq.heappop(min_heap)
    diff = high - low
    print(f"#{test_case} {diff}")
