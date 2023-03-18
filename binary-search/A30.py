# 이진 탐색
# 가사 검색

from bisect import bisect_left, bisect_right

# 값이 [left, right]인 데이터의 개수를 반환하는 함수
# fro?? -> [froaa, frozz]
def count_by_range(a, left, right):
    right_i = bisect_right(a, right)
    left_i = bisect_left(a, left)
    return right_i - left_i

array = [[] for _ in range(10001)]  # 단어를 길이별로 저장
rev_array = [[] for _ in range(10001)]  # 단어를 뒤집어 길이별로 저장

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        rev_array[len(word)].append(word[::-1])  # 단어를 뒤집어 저장

    for i in range(10001):
        array[i].sort()
        rev_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(rev_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)  # 검색된 단어의 개수를 저장
    return answer
            
words = list(input().split())
queries = list(input().split())
print(solution(words, queries))

'''
입력 샘플
frodo front frost frozen frame kakao
fro?? ????o fr??? fro??? pro?
출력 샘플
3 2 4 1 0
'''