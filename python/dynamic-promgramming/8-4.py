# 다이나믹 프로그래밍
# 피보나치 함수
# 메모이제이션 / 캐싱
# 보텀업: 반복문 / 작은 문제 -> 큰 문제
# O(N)

n = int(input())
array = [0] * (n + 1)
array[1], array[2] = 1, 1

for i in range(3, n + 1):
    array[i] = array[i - 1] + array[i - 2]

print(array[n])
