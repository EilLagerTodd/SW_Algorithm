import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, k = map(int, input().split())
tool = [list(map(int, input().split())) for _ in range(n)]
backpack = [[0]]

for x, y in tool:

    print(tool.index([x, y]))
