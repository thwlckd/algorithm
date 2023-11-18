# 상호의 배틀필드

step = {
    "U": [(-1, 0), "^"],
    "D": [(1, 0), "v"],
    "L": [(0, -1), "<"],
    "R": [(0, 1), ">"],
}


def action(command):
    global row, col

    if command == "S":
        shot(row, col)
    else:
        # move
        matrix[row][col] = step[command][1]
        n_row = row + step[command][0][0]
        n_col = col + step[command][0][1]
        if 0 <= n_row < H and 0 <= n_col < W:
            if matrix[n_row][n_col] == ".":
                matrix[row][col] = "."
                matrix[n_row][n_col] = step[command][1]
                row, col = n_row, n_col


def shot(x, y):
    head = matrix[x][y]
    while True:
        if head == "^":
            x -= 1
        elif head == "v":
            x += 1
        elif head == "<":
            y -= 1
        else:
            y += 1

        if x < 0 or x >= H or y < 0 or y >= W:
            return

        if matrix[x][y] == "#":
            return
        elif matrix[x][y] == "*":
            matrix[x][y] = "."
            return


T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    matrix = []
    row, col = 0, 0
    for i in range(H):
        matrix.append(list(input()))
        for j in range(W):
            if matrix[i][j] in ["^", "v", "<", ">"]:
                row, col = i, j

    N = int(input())
    commands = list(input())
    for command in commands:
        action(command)

    print(f"#{test_case}", end=" ")

    for row in matrix:
        print("".join(row))
