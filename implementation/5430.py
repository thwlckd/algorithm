# AC

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
result = list()
for i in range(t):
    functions = list(input())
    n = int(input())
    data = deque(input()[1:-2].split(","))

    flag = False
    reverse = 0
    for fn in functions:
        if fn == "R":
            reverse += 1
        elif fn == "D":
            if len(data) <= 0 or data[0] == "":
                print("error")
                flag = True
                break
            else:
                if reverse % 2 == 1:
                    data.pop()
                else:
                    data.popleft()

    if not flag:
        if reverse % 2 == 1:
            data.reverse()
        print("[" + ",".join(data) + "]")
