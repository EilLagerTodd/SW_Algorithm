import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
infy = 2e9
arr = [infy] * (m+1)
arr[0] = 0
for i in coin:
    for j in range(i, m+1):
        arr[j] = min(arr[j], arr[j-i] + 1)
print(arr[m])
