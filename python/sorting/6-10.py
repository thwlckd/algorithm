# 정렬
# 위에서 아래로

n = int(input())
L = []
for i in range(n):
    L.append(int(input()))

L.sort(reverse=True)
for i in L:
    print(i, end=' ')


# n = int(input())
# L = []
# for i in range(n):
#     L.append(int(input()))

# for i in range(len(L)):
#     min_index = i
#     for j in range(i, len(L)):
#         if L[i] > L[j]:
#             L[i], L[j] = L[j], L[i]
# L.reverse()
# for i in L:
#     print(i, end=' ')