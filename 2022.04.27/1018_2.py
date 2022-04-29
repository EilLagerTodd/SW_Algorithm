import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

m, n = map(int, input().split())
board = [input() for _ in range(m)]
index1 = 0
index2 = 0

for a in range(m-7):
    for b in range(n-7):
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1

print(min(index1, index2))
