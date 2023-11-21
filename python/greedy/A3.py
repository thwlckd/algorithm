# 그리디
# 문자열 뒤집기

s = list(input())
count0 = 0
count1 =0
if s[0] == '1':
    count0 += 1
else:
    count1 += 1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))

# from collections import Counter

# s = list(input())
# counter = Counter(s)
# check = False
# if counter['0'] < counter['1']:
#     check = True
# count = 0
# if check == False:  # 0이 더 많음 -> 1 뒤집기
#     for i in range(1, len(s)):
#         if s[i] != s[i-1] and s[i-1] == '1':
#             count += 1
#     if s[len(s)-1] == '1':
#         count += 1
# else:
#     for i in range(1, len(s)):
#         if s[i] != s[i-1] and s[i-1] == '0':
#             count += 1
#     if s[len(s)-1] == '0':
#         count += 1
# print(count)

'''
입력 샘플
0001100
출력 샘플
1'''