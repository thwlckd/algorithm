# 구현
# 시각

hour = int(input())
minute = 59
second = 59
count = 0

for h in range(hour+1):
    for m in range(minute+1):
        for s in range(second+1):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count += 1

print(count)
