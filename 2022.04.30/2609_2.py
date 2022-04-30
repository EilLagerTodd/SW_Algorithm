import math
import sys
sys.stdin = open("input.txt", "r")

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
