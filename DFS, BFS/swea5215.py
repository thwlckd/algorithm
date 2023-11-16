# 햄버거 다이어트


def dfs(depth, calory, score):
    global result

    if calory > L:
        return

    result = max(result, score)

    for i in range(depth, N):
        if visited[i] == False:
            visited[i] = True
            dfs(i + 1, calory + data[i][1], score + data[i][0])
            visited[i] = False


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]  # [점수, 칼로리]
    visited = [False] * N
    result = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {result}")
