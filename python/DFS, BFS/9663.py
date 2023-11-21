# N-Queen


def dfs(depth):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        if visited[i] == False:
            board[depth] = i

            if check(depth):
                visited[i] = True
                dfs(depth + 1)
                visited[i] = False


def check(n):
    for i in range(n):
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False
    return True


N = int(input())
board = [0] * N
visited = [False] * N
result = 0
dfs(0)
print(result)
