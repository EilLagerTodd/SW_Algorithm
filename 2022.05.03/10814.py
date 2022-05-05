import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
person = [list(input().split()) for _ in range(n)]
person.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(person[i][0], person[i][1])
