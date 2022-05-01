import sys
sys.stdin = open("input.txt", "r")


while True:
    x, y, z = map(int, input().split())
    if x == y == z == 0:
        break

    long = max(x, y, z)
    long2 = long*long
    x2 = x*x
    y2 = y*y
    z2 = z*z

    if long2 == x2 + y2 or long2 == x2 + z2 or long2 == z2 + y2:
        print("right")
    else:
        print("wrong")
