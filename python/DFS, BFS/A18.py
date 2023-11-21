# 괄호 변환
# 재귀함수

def solution(s):
    left = 0
    right = 0
    u = ""
    v = ""
    for now in s:
        if now == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = s[:left+right]
            v = s[left+right:]
            if check(u):  # u = 올바른 괄호 문자열
                v = solution(v)
                return u + v
            else:
                v = solution(v)
                v = "(" + v + ")"
                u = list(u[1:-1])
                u = reverse(u)
                return v + "".join(u)
    return ""  # v = 빈 문자열

def check(s):  # 열고 닫기 -> 닫기 개수가 많아질때 false
    count = 0
    for now in s:
        if now == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def reverse(s):
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
    return s

s = input()
print(solution(s))

'''
입력 샘플 1
(()())()
출력 샘플 1
(()())()
입력 샘플 2
)(
출력 샘플 2
()
입력 샘플 3
()))((()
출력 샘플 3
()(())()
'''