# 회문 1

T = 10

for test_case in range(1, T + 1):
  n = int(input())
  arr = []
  count = 0
  for i in range(8):
    arr.append(list(input()))
    for j in range(0, 8-n+1):
      temp =  arr[i][j:j+n]
      if temp == temp[::-1]:
        count += 1

  for i in range(8):
    for j in range(0, 8-n+1):
      temp = ''
      for k in range(j, j+n):
        temp += arr[k][i]
      if temp == temp[::-1]:
        count += 1

  print(f'#{test_case} {count}')
