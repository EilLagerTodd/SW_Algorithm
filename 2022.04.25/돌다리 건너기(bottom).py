import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [0] * (n+3)
arr[1] = 1
arr[2] = 2

for i in range(3, n+2):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n+1])
