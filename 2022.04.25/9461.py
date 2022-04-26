import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    p = int(input())
    arr = [0] * (102)
    arr[1] = 1
    arr[2] = 1
    arr[3] = 1
    for i in range(4, p+1):
        arr[i] = arr[i-3] + arr[i-2]
    print(arr[p])
