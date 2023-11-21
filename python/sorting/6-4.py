# 퀵 정렬
# O(NlogN)

array = [5, 3, 8, 4, 7, 1, 3, 6, 9, 0]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start  # 첫번째 원소로 피버팅: 호어 분할
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:  # 피벗보다 큰 데이터 찾기
            left += 1
        while right > start and array[right] >= array[pivot]:  # 피벗보다 작은 데이터 찾기
            right -= 1
        if left > right:  # 모든 데이터 탐색
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)


# 파이써닉한 퀵 정렬
array = [5, 3, 8, 4, 7, 1, 3, 6, 9, 0]


def quick_ver_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_ver_python(left_side) + [pivot] + quick_ver_python(right_side)


print(quick_ver_python(array))
