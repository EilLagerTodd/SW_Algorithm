n = int(input())
k = int(input())
card = []
viseted = [0]*n

for i in range(n):
    card.append(int(input()))


# def fow(arr, K):
#     result = []

#     if K == 0:
#         return[[]]
#     for i, elem in enumerate(arr):
#         for P in fow(arr[:i] + arr[i+1:], K-1):
#             result += [[elem]+P]

#     return result


# def fow_2(arr, K, viseted):
#     if K == 0:
#         return

#     for i in range(n):
#         if not viseted[i]:
#             viseted[i] = 1
#             arr[i]
#             fow_2()
#             arr[i]
#             viseted[i] = 0


# def fow_3(arr, K, viseted):
#     result = []

#     if K == 0:
#         return
#     for i in card:
#         for j in card[i]:
#             result += 1


def fow_4(K, viseted):
    result = []

    if K == 0:
        print(result)
        return
    for i in card:
        if not viseted[i]:
            continue
        result.append(card[i])
        viseted[i] = 1
        fow_4(K-1, viseted)
        viseted[i] = 0


new_card = fow_4(k, viseted)

for i in range(len(card)):
    print(i)

print(new_card)
