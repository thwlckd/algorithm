# 톱니바퀴

from collections import deque


def left(i, d):
    if i < 0:
        return
    if gears[i + 1][-2] != gears[i][2]:
        left(i - 1, -d)
        gears[i].rotate(-d)


def right(i, d):
    if i > 3:
        return
    if gears[i - 1][2] != gears[i][-2]:
        right(i + 1, -d)
        gears[i].rotate(-d)


gears = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())
for _ in range(k):
    index, direction = map(int, input().split())
    index -= 1
    left(index - 1, direction)
    right(index + 1, direction)
    gears[index].rotate(direction)

total = 0
for i in range(4):
    if gears[i][0] == 1:
        total += 2**i
print(total)
