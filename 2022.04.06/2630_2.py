n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result = []


def paper_cut(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                paper_cut(x, y, N//2)
                paper_cut(x, y+N//2, N//2)
                paper_cut(x+N//2, y, N//2)
                paper_cut(x+N//2, y+N//2, N//2)
            if color == 0:
                result.append(0)
            elif color == 1:
                result.append(1)


paper_cut(0, 0, n)
print(result.count(0))
print(result.count(1))
