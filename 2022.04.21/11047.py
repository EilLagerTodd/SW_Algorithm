import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
coin = []

for _ in range(n):
    value = int(input())
    if value > m:
        continue
    else:
        coin.append(value)

cnt = 0

for i in reversed(coin):
    while m >= i:
        m = m - i
        cnt += 1

print(cnt)
