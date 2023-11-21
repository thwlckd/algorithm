# 그리디
# 곱하기 혹은 더하기

def calculate(left, right):
    if left * right == 0:
        return left + right
    else:
        return left * right

s = list(input())
result = int(s[0])
for i in range(len(s) - 1):
    result = calculate(result, int(s[i + 1]))

print(result)

'''
입력 샘플
02984
출력 샘플
576
'''