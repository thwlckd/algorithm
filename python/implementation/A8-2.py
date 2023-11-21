# 문자열 재정렬
# 2회차

data = list(input())
alphabet = list()
number = 0
for char in data:
    if "A" <= char <= "Z":
        alphabet.append(char)
    else:
        number += int(char)

alphabet.sort()
alphabet.append(str(number))
for char in alphabet:
    print(char, end="")
