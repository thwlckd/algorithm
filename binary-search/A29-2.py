# 공유기 설치
# 2회차
# 공유기간 최대 거리 구하기 -> 탐색 -> 공유기간 거리를 이진 탐색을 이용해 절반씩 증감

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
left = 1
right = arr[-1] - arr[0]
result = 0
while left <= right:
    mid = (left + right) // 2  # 공유기간 최소 거리
    value = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)
