def solution(s):
    length = len(s)
    answer = length

    for i in range(1, length // 2 + 1):
        result = ""
        prev = s[:i]
        count = 1
        for j in range(i, length, i):
            if prev == s[j : j + i]:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + prev
                else:
                    result += prev
                prev = s[j : j + i]
                count = 1
        if count >= 2:
            result += str(count) + prev
        else:
            result += prev
        answer = min(answer, len(result))
    return answer


print(solution("ababcdcdababcdcd"))
