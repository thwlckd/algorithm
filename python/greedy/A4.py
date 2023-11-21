# 그리디
# 만들 수 없는 금액

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:  # target + x - 1 까지의 모든 금액을 만들 수 있음
        break
    target += x
print(target)

'''
입력 샘플
5
3 2 1 1 9
출력 샘플
8
'''