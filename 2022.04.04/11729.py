n = int(input())


def hanoi(n, x, y):
    if n == 0:
        return

    hanoi(n-1, x, 6-x-y)
    print(x, y)
    hanoi(n-1, 6-x-y, y)


print(2 ** n - 1)
hanoi(n, 1, 3)
