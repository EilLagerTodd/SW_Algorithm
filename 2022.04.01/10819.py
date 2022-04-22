import itertools

n = int(input())
card = list(map(int, input().split()))
card.sort()
card_2 = list(itertools.permutations(card, n))
max_result = 0

for i in range(len(card_2)) :
    cur = 0
    for j in range(0, n-1) :
        cur += abs(card_2[i][j] - card_2[i][j + 1])
    if cur > max_result:
        max_result = cur

print(max_result)

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# arr2 = list(itertools.permutations(arr, n))
# res = 0
# for i in range(len(arr2)):
#     cur = 0
#     for j in range(0, n - 1):
#         cur += abs(arr2[i][j] - arr2[i][j + 1])
#     if cur > res:
#         res = cur
# print(res)
