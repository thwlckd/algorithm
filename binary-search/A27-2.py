# 정렬된 배열에서 특정 수의 개수 구하기

# bisect library를 이용한 풀이
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect_left(arr, x)
right = bisect_right(arr, x)
result = right - left

if result == 0:
    print(-1)
else:
    print(result)


# 이진탐색을 이용한 풀이
n, x = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(arr, left, right, target):
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


index = binary_search(arr, 0, n - 1, x)
if index:
    left, right = index, index
    while True:
        if arr[left - 1] == x:
            left -= 1
        else:
            break
    while True:
        if arr[right + 1] == x:
            right += 1
        else:
            break
    print(right - left + 1)
else:
    print(-1)
