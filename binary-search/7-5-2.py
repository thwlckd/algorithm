# 부품 찾기
# 2회차

import sys

input = sys.stdin.readline

n = int(input())
store = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))


def binary_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, end, target)


store.sort()
result = []
for target in arr:
    temp = binary_search(store, 0, n - 1, target)
    result.append("yes" if temp else "no")

print(" ".join(result))
