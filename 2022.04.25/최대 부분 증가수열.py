import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n = int(input())
number = [0] + list(map(int, input().split()))
number[1] = 1
dy = [0] * (n+1)
res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if number[j] < number[i] and dy[j] > max:
            max = dy[j]
        dy[i] = max + 1
        if dy[i] > res:
            res = dy[i]
print(res)
