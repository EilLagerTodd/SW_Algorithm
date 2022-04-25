import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * (n+1)

if n == 1:
    print(1)
else:
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = (arr[i-2] + arr[i-1])
    print(arr[n] % 10007)
