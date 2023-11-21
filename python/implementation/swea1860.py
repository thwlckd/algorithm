# 진기의 최고급 붕어빵

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrived = list(map(int, input().split()))
    arrived.sort()
    store = 0
    time = 0

    result = "Possible"
    for customer in arrived:
        if store < 1:
            time += M
            store += K
        if customer - time < 0:
            result = "Impossible"
            break
        store -= 1

    print(f"#{test_case} {result}")
