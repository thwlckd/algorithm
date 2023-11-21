# 프린터 큐
# 2회차

from collections import deque

cases = int(input())
result = []

for _ in range(cases):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    i = 0
    while q:
        to_pop = max(q)
        first = q.popleft()
        m -= 1
        if to_pop == first:
            i += 1
            if m == -1:
                print(i)
                break
        else:
            q.append(first)
            if m == -1:
                m = len(q) - 1
