# 이진 탐색
# 부품 찾기

n = int(input())
n_data = list(map(int, input().split()))
m = int(input())
m_data = list(map(int, input().split()))

n_data.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in range(m):
    result = binary_search(n_data, m_data[i], 0, n - 1)
    if result == None:
        print("no", end=' ')
    else:
        
        print("yes", end=' ')

