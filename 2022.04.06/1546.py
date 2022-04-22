n = int(input())
arr = list(map(int, input().split()))
arr_max = max(arr)
result = 0

for i in range(n):
    result += arr[i]/arr_max*100

print(result/n)
