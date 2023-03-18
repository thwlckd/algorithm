# 이진 탐색
# 공유기 설치
# 인접한 두 공유기 사이의 거리를 조절해가며 공유기 설치
# 인접한 두 공유기 사이 거리의 최댓값 = right
# 인접한 두 공유기 사이 거리의 최솟값 = left
# 현재 탐색중인 거리 = mid

n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()

result = 0
left = 1  # min gap
right = data[-1] - data[0]  # max gap
while left <= right:
    mid = (left+right) // 2  # now gap
    value = data[0]  # 가장 최근에 공유기를 설치한 위치
    count = 1
    for i in range(1, n):  # 앞에서 부터 공유기 설치
        if data[i] >= value + mid:
            value = data[i]
            count += 1
    if count >= c:  # c개 이상 공유기를 설치할 수 있는 경우, 거리 증가
        left = mid + 1
        result = mid
    else:  # c개 이상 공유기를 설치할 수 없는 경우, 거리 감소
        right = mid - 1

print(result)

'''
입력 샘플
5 3
1
2
8
4
9
출력 샘플
3
'''