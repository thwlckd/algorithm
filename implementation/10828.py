# 스택

import sys

input = sys.stdin.readline

n = int(input())
stack = list()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        print(stack.pop()) if len(stack) > 0 else print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1) if len(stack) == 0 else print(0)
    elif command[0] == "top":
        print(stack[-1]) if len(stack) > 0 else print(-1)
