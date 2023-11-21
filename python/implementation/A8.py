# 구현
# 문자열 재정렬

data = list(input())
alphabet = []
num = 0
for i in range(len(data)):
    if 'A' <= data[i] <= 'Z':  # or data[i].isalpha()
        alphabet.append(data[i])
    else:
        num += int(data[i])
alphabet.sort()
alphabet.append(str(num))
for i in range(len(alphabet)):  # or print(''.join(alphabet))
    print(alphabet[i], end='')

'''
입력 샘플
K1KA5CB7
출력 샘플
ABCKK13
'''