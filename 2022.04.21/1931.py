import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(start, end):
    cnt = 0
    for a, b in room:
        if a >= end:
            end = b
            cnt += 1
    print(cnt)


n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
room.sort(key=lambda x: (x[1], x[0]))

find(0, 0)
