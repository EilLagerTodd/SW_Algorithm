import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())
    if z % x == 0:
        first = x
        end = z
    else:
        first = (z % x)
        end = (z // x) + 1
    print(first*100+end)
