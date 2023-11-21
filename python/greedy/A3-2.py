# 문자열 뒤집기
# 2회차 풀이

s = list(input())
count = [0, 0]
before = s[0]
count[int(before)] += 1

for i in range(1, len(s)):
    if before != s[i]:
        before = s[i]
        count[int(before)] += 1

print(min(count))
