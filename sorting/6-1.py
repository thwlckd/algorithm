# 선택정렬
# O(N^2)

array = [5, 3, 8, 4, 7, 1, 3, 6, 9, 0]

for i in range(len(array)):
    min_i = i
    for j in range(i + 1, len(array)):
        if array[min_i] > array[j]:
            min_i = j
    array[min_i], array[i] = array[i], array[min_i]

print(array)
