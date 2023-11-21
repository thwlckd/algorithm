# 정렬
# 두 배열의 원소 교체

# 정렬
# 두 배열의 원소 교체

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if B[i] > A[i]:
        B[i], A[i] = A[i], B[i]
    else:
        break

print(sum(A))


# n, k = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# A.sort()
# B.sort(reverse=True)

# for i in range(k):
#     if B[0] > A[0]:
#         A.append(B[0])
#         B.append(A[0])
#         A.pop(0)
#         B.pop(0)
#     else:
#         break

# print(sum(A))
