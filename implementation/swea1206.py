# View

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    buildings = [0, 0] + list(map(int, input().split())) + [0, 0]
    count = 0
    for i in range(len(buildings) - 2):
        now = buildings[i]
        max_height = max(
            buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2]
        )
        if now > max_height:
            count += now - max_height
    print(f"#{test_case} {count}")


# 1
# 10
# 3 5 2 4 9 0 6 4 0 6
