# 이진 탐색
# 떡볶이 떡 만들기
# 파라메트릭 서치 유형: 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법 -> 이진 탐색

n, m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in array:
        if i > mid:
            sum += i - mid
    if sum == m:
        result = mid
        break
    elif sum < m:
        end = mid - 1
    else:
        start = mid + 1
print(result)
