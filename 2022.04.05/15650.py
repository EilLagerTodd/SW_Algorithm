n, m = map(int, input().split())
arr = []


def check(start, k):
    if k == m:
        for i in range(m):
            print(' '.join(map(str, arr)))
        arr.clear()
        return
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            check(i+1, k+1)


check(1, 0)
