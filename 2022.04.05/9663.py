def fow(k):
    global cnt
    if k == n:
        cnt += 1
        return

    else:
        for i in range(n):
            arr[k] = i
            for j in range(n):
                if arr[j] == arr[k] or (arr[k] - k) == (arr[j] - j) or (arr[k] + k) == (arr[j] + j):
                    break
                else:
                    fow(k+1)


n = int(input())
arr = [0] * n
cnt = 0
fow(0)
print(cnt)
