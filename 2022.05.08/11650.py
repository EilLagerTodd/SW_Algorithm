import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(arr[i][0], arr[i][1], sep=' ')