# 비밀번호

T = 10

for test_case in range(1, T + 1):
    n, pwd = input().split()
    n, pwd = int(n), list(pwd)

    new_pwd = []
    for now in pwd:
        if not len(new_pwd):
            new_pwd.append(now)
        elif new_pwd[-1] == now:
            new_pwd.pop()
        else:
            new_pwd.append(now)

    print(f"#{test_case} {''.join(new_pwd)}")
