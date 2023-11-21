# 이진 탐색
# 고정점 찾기

def binary_search(array, left, right):  # key = array[mid]
    if left > right:
        return None
    mid = (left + right) // 2
    key = array[mid]
    if key == mid:
        return key
    elif key < mid:
        return binary_search(array, mid + 1, right)
    else:
        return binary_search(array, left, mid - 1)

n = int(input())
data = list(map(int, input().split()))
result = binary_search(data, 0, n - 1)
if result == None:
    print(-1)
else:
    print(result)

'''
입력 샘플 1
5
-15 -6 1 3 7
출력 샘플 1
3
입력 샘플 2
7
-15 -4 3 8 9 13 15
출력 샘플 2
-1
'''