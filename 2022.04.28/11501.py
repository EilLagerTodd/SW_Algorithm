import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    t = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    value = 0
    maximum = 0

    for i in arr:
        if i > maximum:
            maximum = i
        else:
            value += maximum - i
    print(value)
