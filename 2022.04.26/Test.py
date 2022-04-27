import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
DP = [[0]*(n) for _ in range(n)]

for i in range(1, n):
    for j in range(1, n):
        pass
