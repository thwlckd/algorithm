# 회문 2

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    data = [list(input()) for _ in range(100)]
    result = 0
    for i in range(100):
        for j in range(100):
            for k in range(j + 1, 100):
                word = data[i][j:k]
                if word == word[::-1]:
                    result = max(result, len(word))

    for i in range(100):
        for j in range(100):
            word = ""
            for k in range(j, 100):
                word += data[k][i]
                if word == word[::-1]:
                    result = max(result, len(word))

    print(f"#{test_case} {result}")
