n, m = map(int, input().split())
arr = []
visited = [False] * n


def check(k):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            arr.append(i+1)
            check(k+1)
            visited[i] = False
            arr.pop()


check(0)
