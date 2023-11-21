# 곱하기 혹은 더하기
# 2회차 풀이

s = list(input())
result = int(s[0])

for i in range(len(s) - 1):
    data = int(s[i + 1])
    if result * data != 0:
        result = result * data
    else:
        result = result + data

print(result)
