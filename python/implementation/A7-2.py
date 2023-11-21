# 럭키 스트레이트
# 2회차 풀이

n = list(input())
left, right = n[: len(n) // 2], n[len(n) // 2 :]
left_sum = 0
right_sum = 0

for i in range(len(n) // 2):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
