import sys
sys.stdin = open("input.txt", "r")

A, B = map(int, input().split())
x, y = A, B

while y != 0:
    x = x % y
    x, y = y, x

print(x)
print((A*B)//x)
