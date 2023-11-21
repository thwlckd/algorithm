# 구현
# 게임 개발

n, m = map(int, input().split())
x, y, head = map(int, input().split())
mtx = list()
for _ in range(n):
    mtx.append(list(map(int, input().split())))
mtx[x][y] = 2  # 방문 육지 2
dx = [0, 1, 0, -1]  # 북동남서
dy = [1, 0, -1, 0]

def turn_left():
    global head  # 전역 변수 head
    head -= 1
    if head == -1:
        head = 3

count = 1
turn_time = 0
while(True):
    turn_left()
    if mtx[x + dx[head]][y + dy[head]] == 0:
        x = x + dx[head]
        y = y + dy[head]
        mtx[x][y] = 2
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        turn_time = 0
        if mtx[x - dx[head]][y - dy[head]] == 2:
            x = x - dx[head]
            y = y - dy[head]
        else:
            break

print(count)


# n, m = map(int, input().split())
# x, y, head = map(int, input().split())  # head:0123 / 북동남서
# map = []

# for i in range(n):
#     line = input().split()
#     map.append(line)

# dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]  # 북동남서

# def turn_left(head, count):
#     if head == 0:
#         head = 3
#     elif head == 1:
#         head = 0
#     elif head == 2:
#         head = 1
#     elif head == 3:
#         head = 2
#     else:
#         print("wrong head!")
#     count += 1
    
#     return head, count

# visited = {(x, y)}
# cnt = 0

# while(True):
#     head, cnt = turn_left(head, cnt)
#     print(visited)
#     if (x + dx[head], y + dy[head]) not in visited and map[x + dx[head]][y + dy[head]] != '1':
#         x = x + dx[head]
#         y = y + dy[head]
#         visited.add((x, y))
#         cnt = 0

#     if cnt >= 4:  # 한 칸 뒤로
#         if map[x - dx[head]][y - dy[head]] != '1':
#             x = x - dx[head]
#             y = y - dy[head]
#             cnt = 0
#         else:
#             x = x - dx[head]
#             y = y - dy[head]
#             print(x, y, "/", cnt, "/", head)
#             break

    
#     print(x, y, "/", cnt, "/", head)

# print(len(visited))