import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
dp = [0] * (n)
dp[0] = arr[0]
result = 0

for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]


print(sum(dp))
