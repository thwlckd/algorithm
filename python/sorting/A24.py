# 정렬
# 안테나

n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[(n - 1) // 2])

'''
입력 샘플
4
5 1 7 9
출력 샘플
5
'''