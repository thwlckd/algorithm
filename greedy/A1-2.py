# 모험가 길드
# 2회차 풀이

n = int(input())
data = list(map(int, input().split()))
count = 0
result = 0

data.sort()

for member in data:
    count += 1
    if count >= member:
        result += 1
        count = 0

print(result)
