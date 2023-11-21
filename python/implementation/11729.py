# 하노이 탑 이동 순서


def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    middle = 6 - start - end  # (1+2+3)-start-end -> 나머지 하나의 기둥
    hanoi(n - 1, start, middle)
    print(start, end)
    hanoi(n - 1, middle, end)


n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)
