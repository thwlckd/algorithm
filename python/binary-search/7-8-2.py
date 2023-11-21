# 떡볶이 떡 만들기
# 2회차

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)
result = 0
while left <= right:
    total = 0
    mid = (left + right) // 2
    for now in arr:
        temp = now - mid
        if temp > 0:
            total += temp
    if total < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)
