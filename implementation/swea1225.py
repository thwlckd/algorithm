# 암호생성기

from collections import deque

T = 10

for test_case in range(1, T + 1):
  n = int(input())
  q = deque(map(int, input().split()))
  i = 0
  while True:
    i = i % 5
    temp = q.popleft() - (i+1)
    if temp <= 0:
      q.append(0)
      break
    q.append(temp)
    i += 1
  print(f'#{test_case} ', end='')
  for value in q:
    print(value, end=' ')
  print()
    
  


  