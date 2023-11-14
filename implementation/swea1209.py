# Sum

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    sum_arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
        sum_arr.append(sum(arr[i]))

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        sum_arr.append(temp)

    temp1 = 0
    temp2 = 0
    for i in range(100):
        temp1 += arr[i][i]
        temp2 += arr[99 - i][i]
    sum_arr.append(temp1)
    sum_arr.append(temp2)

    print(f"#{test_case} {max(sum_arr)}")
