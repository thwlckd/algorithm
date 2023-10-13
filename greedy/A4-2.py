# 만들 수 없는 금액
# 2회차 풀이

n = int(input())
data = list(map(int, input().split()))

data.sort()
min = 1

for now in data:
    # 1 ~ 5의 숫자를 만들 수 있을 때, 6보다 작은 수가 오면 1 ~ 11(5+6)의 숫자를 만들 수 있음
    # 6보다 큰 수가 오면 6부터 큰수 -1 까지 만들 수 없음 -> min == 6
    if min < now:
        break
    min += now

print(min)
