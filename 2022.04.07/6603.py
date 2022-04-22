from itertools import combinations
arr = list(map(int, input().split()))

# while True:
#     N = list(map(int, input().split()))
#     if N[0] == 0:
#         break
#     else:
#         for i in range(1, int(N[0]+1)):
#             print(i)


s = list(combinations(arr[1:], 6))
print(s)
