# 구현
# 상하좌우
# x, y = 1 ,1  /  dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  /  move_type = ['L', 'R', 'U', 'D'] 으로 하는 방법도 가능

n = int(input())
data = input().split()

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # L, R ,U ,D
coordinate = [1, 1]

def move(dir, coor):
    before_coor = coor
    if dir == 'U':
        coor = [coor[0] -1, coor[1]]
    elif dir == 'D':
        coor = [coor[0] + 1, coor[1]]
    elif dir == 'L':
        coor = [coor[0], coor[1] - 1]
    elif dir == 'R':
        coor = [coor[0], coor[1] + 1]
    else:
        print("wrong input")
    
    if coor[0] > 0 and coor[0] <= n and coor[1] > 0 and coor[1] <= n:
        return coor
    else:
        print("out of range!")
        return before_coor

for i in range(n+1):
    coordinate = move(data[i], coordinate)

print(coordinate)