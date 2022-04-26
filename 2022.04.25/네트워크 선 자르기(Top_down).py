import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def top(n):
    if arr[n] > 0:
        return arr[n]
    if n == 1 or n == 2:
        return n
    else:
        arr[n] = top(n-1) + top(n-2)
        return arr[n]


n = int(input())
arr = [0] * (n+1)
print(top(n))
