# 구현
# 문자열 압축
# 완전 탐색
# 2020 카카오 신입 공채 기출

def solutions(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:  # 반복 문자열 발생
                count += 1  # 반복 횟수
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
s = input()    
print(solutions(s))

'''
입력 샘플 1
aabbaccc
출력 샘플 1
7
입력 샘플 2
ababcdcdababcdcd
출력 샘플 2
9
입력 샘플 3
abcabcabcabcdededededede
출력 샘플 3
14
'''