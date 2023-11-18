# 정곤이의 단조 증가하는 수

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    arr = []
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            num = list(str(data[i] * data[j]))
            high = 0
            flag = True
            for now in num:
                if int(now) >= high:
                    high = int(now)
                else:
                    flag = False
                    break
            if flag:
                arr.append(int("".join(num)))
    print(f"#{test_case} {max(arr) if len(arr) else -1}")
