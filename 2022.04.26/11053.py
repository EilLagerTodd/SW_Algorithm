import sys
input = sys.stdin.readline


n = int(input())
number = list(map(int, input().split()))
dy = [0] * n

for i in range(n):
    for j in range(i):
        if number[i] > number[j] and dy[i] < dy[j]:
            dy[i] = dy[j]
    dy[i] += 1
print(max(dy))
