# String

T = 10
for test_case in range(1, T + 1):
    n = int(input())
    search = input()
    sentence = input()
    count = 0
    for i in range(len(sentence) - len(search) + 1):
        if sentence[i : i + len(search)] == search:
            count += 1
    print(f"#{test_case} {count}")
