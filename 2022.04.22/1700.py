import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(n):
    plug.append(arr[i])

for i in arr[n:]:
    if i in plug:
        continue
    else:
        plug.append(i)
        cnt += 1

print(cnt)
