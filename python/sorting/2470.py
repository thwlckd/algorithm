# 두 용액

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left, right = 0, n - 1
sum = abs(arr[left] + arr[right])
value = [arr[left], arr[right]]
while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < sum:
        sum = abs(temp)
        value = [arr[left], arr[right]]
    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        break

print(value[0], value[1])
