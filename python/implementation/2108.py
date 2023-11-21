# 통계학

import sys

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

avg = round(sum(data) / n)

data.sort()
center = data[int(n / 2)]

data_dict = {}
for num in data:
    if num in data_dict:
        data_dict[num] += 1
    else:
        data_dict[num] = 1

max_count = max(data_dict.values())
max_count_list = list()
for key in data_dict:
    if data_dict[key] == max_count:
        max_count_list.append(key)

if len(max_count_list) > 1:
    max_frequency = max_count_list[1]
else:
    max_frequency = max_count_list[0]

data_range = data[-1] - data[0]

print(avg)
print(center)
print(max_frequency)
print(data_range)
