import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
number = [0] + list(map(int, input().split()))
hap = [0]*(n+1)
hap[1] = number[1]
hap[2] = number[1] + number[2]

for i in range(3, n+1):
    hap[i] = hap[i-1] + number[i]

for i in range(m):
    a, b = map(int, input().split())
    print(hap[b] - hap[a-1])
