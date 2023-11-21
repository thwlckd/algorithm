# 이진 탐색
# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x= map(int, input().split())
data = list(map(int, input().split()))
left = bisect_left(data, x)
right = bisect_right(data, x)
result = right - left
if result == 0:
    print(-1)
else:
    print(result)

# from collections import Counter

# n, x= map(int, input().split())
# data = list(map(int, input().split()))
# counter = Counter(data)
# result = counter[x]
# if result == 0:
#     print(-1)
# else:
#     print(counter[x])

'''
입력 샘플 1
7 2
1 1 2 2 2 2 3
출력 샘플 1
4
입력샘플 2
7 4
1 1 2 2 2 2 3
출력 샘플 2
-1
'''