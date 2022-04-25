import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

D = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, len(D)):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + D[i][0]
    D[i][1] = min(D[i-1][0], D[i-1][2]) + D[i][1]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + D[i][2]

print(min(D[n-1][0], D[n-1][1], D[n-1][2]))
