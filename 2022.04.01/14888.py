import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, total)
        maximum = max(minimum, total)

    if plus:
        dfs(depth, total + num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth, total - num[depth], plus-1, minus, multiply, divide)
    if multiply:
        dfs(depth, total * num[depth], plus-1, minus, multiply, divide)
    if divide:
        dfs(depth, ( total//num[depth] ), plus-1, minus, multiply, divide)


dfs(1, num[0], op[0], op[1], op[2], op[3])
