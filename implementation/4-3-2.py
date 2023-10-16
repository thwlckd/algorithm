# 왕실의 나이트
# 2회차 풀이

position = input()
row = int(position[1])
column = ord(position[0]) - ord("a") + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
count = 0

for step in steps:
    if (
        1 <= row + step[0]
        and row + step[0] <= 8
        and 1 <= column + step[1]
        and column + step[1] <= 8
    ):
        count += 1

print(count)
