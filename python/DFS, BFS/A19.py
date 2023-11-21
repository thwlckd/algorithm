# 
# 연산자 끼워 넣기

n = int(input())
data = list(map(int, input().split()))
add ,sub, mul, div = map(int, input().split())

min_val = int(1e9)
max_val = int(-1e9)

def dfs(i, now):
    global min_val, max_val, add ,sub, mul, div

    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_val)
print(min_val)

'''
입력 샘플 1
2
5 6
0 0 1 0
출력 샘플 1
30
30
입력 샘플 2
3
3 4 5
1 0 1 0
출력 샘플 2
35
17
입력 샘플 3
6
1 2 3 4 5 6
2 1 1 1
출력 샘플 3
54
-24
'''