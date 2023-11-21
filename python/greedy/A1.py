# 그리디
# 모험가 길드

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0  # 그룹 수
count = 0  # 현재 그룹에 포함된 모험가 수
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# group = []
# cnt = 0
# for i in range(n):
#     element = data[i]
#     group.append(element)
#     if len(group) == element:
#         group.clear()
#         cnt += 1
# print(cnt)