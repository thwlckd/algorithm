# 구현
# 왕실의 나이트

xy = input()
x = int(xy[1])
y = ord(xy[0])  # ord: string to ascii <-> str
y = y - ord('a') + 1
count = 0
move_types = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]  # step

for dx, dy in move_types:
    if x + dx < 1 or x + dx > 8 or y + dy < 1 or y + dy > 8: 
        continue
    else:
        count += 1

print(count)