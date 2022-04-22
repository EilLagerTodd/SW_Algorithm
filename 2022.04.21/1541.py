import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

a = input().split('-')

hap = 0
for i in a[0].split('+'):
    hap += int(i)

for i in a[1:]:
    for j in i.split('+'):
        hap -= int(j)

print(hap)
