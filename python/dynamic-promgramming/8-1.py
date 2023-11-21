# 다이나믹 프로그래밍
# 동적 계획법
# 피보나치 함수
# O(2^N)
# an = an-1 + an-2

n = int(input())

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(n))
