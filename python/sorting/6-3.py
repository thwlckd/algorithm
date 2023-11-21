# 삽입정렬
# O(N^2)
# 배열이 거의 정렬되어 있을때 효율적

array = [5, 3, 8, 4, 7, 1, 3, 6, 9, 0]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
