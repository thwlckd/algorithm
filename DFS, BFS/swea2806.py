# N-Queen


def dfs(depth):
  global result

  if depth == n:
    result += 1
    return
  
  for i in range(n):
    if visited[i] == False:
      board[depth] = i

      if is_promise(depth):
        visited[i] = True
        dfs(depth+1)
        visited[i] = False


def is_promise(row):
  for i in range(row):
    if (board[row] == board[i]) or (row - i == abs(board[row] - board[i])):
      return False
  return True


T = int(input())

for test_case in range(1, T + 1):
  n = int(input())
  board = [0] * n
  visited = [False] * n
  result = 0
  dfs(0)
  print(f'#{test_case} {result}')