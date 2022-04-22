def fibo(n):
    arr[0] = 1
    arr[1] = 2

    if n < 2:
        return arr[n]

    for i in range(2, n+1):
        arr[i] = (arr[i-2] + arr[i-1])%15746

    return arr[n]


n = int(input())
arr = [0 for _ in range(n+2)]

print(fibo(n-1))
