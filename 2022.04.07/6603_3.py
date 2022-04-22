def fow(arr, K):
    result = []

    if K == 0:
        return[[]]
    for i, elem in enumerate(arr):
        for P in fow(arr[:i] + arr[i+1:], K-1):
            result += [[elem]+P]

    return result


def fow_2(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(nums[n])
    fow_2(n + 1, ans)
    ans.pop()
    fow_2(n + 1, ans)


fow_2(0, [])
nums = [1, 2, 3, 4, 5]
answer_list = []
arr = list(map(int, input().split()))
k = arr[0]


print(answer_list)
