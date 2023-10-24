# 수 묶기

n = int(input())
negative = []
positive = []
max_sum = 0
for _ in range(n):
    temp = int(input())
    if temp <= 0:  # 0은 음수에
        negative.append(temp)
    elif temp == 1:
        max_sum += 1
    else:
        positive.append(temp)

negative.sort()
positive.sort(reverse=True)

length = 0
if len(negative) % 2 == 0:
    length = len(negative)
else:
    length = len(negative) - 1
    max_sum += negative[length]
for i in range(0, length, 2):
    max_sum += negative[i] * negative[i + 1]

length = 0
if len(positive) % 2 == 0:
    length = len(positive)
else:
    length = len(positive) - 1
    max_sum += positive[length]
for i in range(0, length, 2):
    max_sum += positive[i] * positive[i + 1]

print(max_sum)
