# 정렬
# 성적이 낮은 순서로 학생 출력하기

n = int(input())
array = []

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array.sort(key=lambda student: student[1])
for i in array:
    print(i[0], end=' ')