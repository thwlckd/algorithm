# ATM

n = int(input())
times = list(map(int, input().split()))
sum = 0
times.sort()

for i in range(len(times)):
    sum += times[i] * (len(times) - i)

print(sum)
