# 농작물 수확하기

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, (list(input())))))
    center = n // 2
    start = center
    end = center + 1
    total = 0
    for i in range(n):
        total += sum(arr[i][start:end])
        if i < center:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f"#{test_case} {total}")
