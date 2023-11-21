# 다이나믹 프로그래밍
# 피보나치 함수
# 메모이제이션 / 캐싱
# 탑다운: 재귀함수 / 큰 문제 -> 작은 문제
# O(N)
# 재귀 제한 완화: sys.setrecursionlimit()

n = int(input())
array = [0] * (n + 1)

def memo_fibo(x):
    if x == 1 or x == 2:
        return 1
    if array[x] != 0:
        return array[x]
    else:
        array[x] = memo_fibo(x - 1) + memo_fibo(x - 2)
    return array[x]

print(memo_fibo(n))
