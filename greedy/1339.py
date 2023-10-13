# 단어 수학

n = int(input())
data = {}

for _ in range(n):
    word = input()
    for i in range(len(word)):
        if word[i] in data:
            data[word[i]] += 10 ** (len(word) - i - 1)
        else:
            data[word[i]] = 10 ** (len(word) - i - 1)

num_list = list(data.values())
num_list.sort(reverse=True)
operand = 9
result = 0
for i in range(len(num_list)):
    result += operand * int(num_list[i])
    operand -= 1

print(result)
