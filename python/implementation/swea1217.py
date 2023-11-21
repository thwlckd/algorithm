# 거듭 제곱


def recrusive(base, exp, count):
    global result
    if exp == count:
        result = base
        return
    recrusive(base * a, exp, count + 1)


T = 10

for test_case in range(1, T + 1):
    n = int(input())
    a, b = map(int, input().split())
    result = 0
    recrusive(a, b, 1)
    print(f"#{test_case} {result}")
