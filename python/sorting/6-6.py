# 계수정렬
# 데이터 크기 범위만큼의 배열을 선언할 수 있을때 사용 -> 일반적으로 100000 넘지 않을 때
# 동일한 값을 가지는 데이터가 여러개 존재할때 적잡
# O(N+K) -> 데이터 최대값 K

array = [5, 3, 8, 4, 7, 1, 3, 6, 9, 0]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 데이터에 해당하는 인덱스의 값 + 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")  # 등장한 횟수만큼 인덱스 출력
