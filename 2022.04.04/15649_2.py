n, m = map(int, input().split())
num = []
numBoolean = [False] * n


def fow(k):
    if k == m:
        print(' '.join(map(str, num)))
        return
    for i in range(n):
        if not numBoolean[i]:
            numBoolean[i] = True
            num.append(i+1)
            fow(k+1)
            numBoolean[i] = False
            num.pop()


fow(0)
