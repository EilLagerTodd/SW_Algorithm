import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(input().rstrip()) for _ in range(m)]
point = board[0][0]
cnt = 0
print(board)
for i in range(1, m):
    if board[i] == board[i-1]:
        if board[i-1] == 'B':
            board[i] == 'W'
            cnt += 1
        else:
            board[i] == 'B'
            cnt += 1
    for j in range(1, n):
        if board[i][j] == board[i][j-1]:
            if board[i][j-1] == 'B':
                board[i][j] == 'W'
                cnt += 1
            else:
                board[i][j] == 'B'
                cnt += 1

print(cnt)
