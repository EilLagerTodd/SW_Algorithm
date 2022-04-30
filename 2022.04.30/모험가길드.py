n = int(input())
arr = list(map(int, input().split()))
result = 0
count = 0

for i in arr:
    result += 1
    if result >= i:
        result = 0
        count += 1

print(count)
