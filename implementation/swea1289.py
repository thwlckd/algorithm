# 원재의 메모리 복구하기

T = int(input())
for test_case in range(1, T + 1):
  data = list(input())
  count = 0
  before = '0'
  for char in data:
    if char != before:
      count += 1
    before = char
  print(f'#{test_case} {count}')