# 부분 수열의 합

def dfs(depth, acc):
  global count
  if acc == k:
    count += 1
    return
  
  if depth == n or acc > k:
    return
  
  for i in range(depth, n):
    if visited[i] == False:
      visited[i] = True
      dfs(i + 1, acc + arr[i])
      visited[i] = False

T = int(input())

for test_case in range(1, T + 1):
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  count = 0
  visited = [False] * n
  dfs(0, 0)
  print(f'#{test_case} {count}')
