# 구현
# 럭키 스트레이트

n = list(input())
half = int(len(n)/2)
left = n[:half]
right = n[half:]
left_sum = 0
right_sum = 0
for i in range(half):
    left_sum += int(left[i])
    right_sum += int(right[i])
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

'''
입력 샘플
123402
출력 샘플
LUCKY
'''