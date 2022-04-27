import sys


n = int(input())
number = list(sys.stdin.readline().rstrip())
hap = 0
for i in range(n):
    hap += int(number[i])
print(hap)
