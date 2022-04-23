import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
infy = 2e9
d = [infy] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != infy:
            d[j] = min(d[j], d[j - arr[i]]+1)


if d[m] == infy:
    print(-1)
else:
    print(d[m])
