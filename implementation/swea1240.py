# 단순 2진 암호코드

mapper = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(input())

    index = 0
    for i in range(n):
        if "1" in arr[i]:
            index = i
            break

    start = 0
    for i in range(m - 1, 0, -1):
        if arr[index][i] == "1":
            start = i - 55
            break

    odd = []
    even = []
    for i in range(8):
        code = arr[index][start : start + 7]
        if i % 2 == 0:
            odd.append(mapper[code])
        else:
            even.append(mapper[code])
        start += 7

    result = 0
    if (sum(odd) * 3 + sum(even)) % 10 == 0:
        result = sum(odd) + sum(even)

    print(f"#{test_case} {result}")
