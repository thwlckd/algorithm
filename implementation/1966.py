# 프린터 큐
# heapq
# max heap -> push(q, (-n, n))

from collections import deque

t = int(input())  # 테스트 케이스
for _ in range(t):
    n, index = map(int, input().split())
    q = deque(list(map(int, input().split())))

    count = 0
    while q:
        max_val = max(q)
        now = q.popleft()
        index -= 1
        if max_val == now:  # 최댓값이 맨 앞에 있는 경우
            count += 1
            if index < 0:  # key의 위치가 맨 앞에서 최댓값인 경우
                print(count)
                break
        else:  # 최댓값이 맨 앞이 아닌 경우
            q.append(now)  # 맨 뒤에 붙임
            if index < 0:  # key의 위치가 맨 앞에서 최댓값이 아닌 경우
                index = len(q) - 1
        
'''
입력 예시
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
출력 예시
1
2
5
'''