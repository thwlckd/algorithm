# 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: (x[1], x[0]))
count = 0  # 경과 시간
result = 0
for i in range(n):
    if array[i][0] >= count:
        count = array[i][1]
        result += 1

print(result)

'''
입력 샘플
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
출력 샘플
4
'''