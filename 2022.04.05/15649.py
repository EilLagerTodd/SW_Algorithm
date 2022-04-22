n, m = map(int, input().split())
arr = [] * n
isused = [False] * n


def fow(k):
    if k == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(n):
        if isused[i] != True:
            arr.append(i+1)
            isused[i] = True
            fow(k+1)
            isused[i] = False
            arr.pop()


fow(0)
