import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * (m+1)

for i in range(n):
    v, k = map(int, input().split())
    for j in range(v, m+1):
        arr[j] = max(arr[j], arr[j-v]+k)
print(arr[m])
