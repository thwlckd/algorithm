# 고정점 찾기
# 2회차

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == mid:
        print(mid)
        break
    elif arr[mid] > mid:
        right = mid - 1
    else:
        left = mid + 1
