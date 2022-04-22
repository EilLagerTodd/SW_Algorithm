import sys
n = int(sys.stdin.readline())


def hanoi(n, x, y):
    if n > 1:
        hanoi(n-1, x, 6-x-y)
    print(x, y)
    if n > 1:
        hanoi(n-1, 6-x-y, y)


if n <= 20:
    print((n-1)**2+n)
    hanoi(n, 1, 3)
