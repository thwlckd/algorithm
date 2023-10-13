# 잃어버린 괄호

data = input().split("-")
result = 0

for i in range(len(data)):
    sum = 0
    for j in data[i].split("+"):
        sum += int(j)
    if i == 0:
        result += sum
    else:
        result -= sum

print(result)
