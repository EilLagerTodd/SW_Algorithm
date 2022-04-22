import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
cards_array = [sys.stdin.readline().rstrip() for _ in range(n)]
array = set()


def permutation(cnt, perm, visit):
    global cards_array
    if cnt == k:
        array.add(''.join(perm))
        return
    for idx in range(n):
        if not visit[idx]:
            visit[idx] = 1
            permutation(cnt+1, perm+[cards_array[idx]], visit)
            visit[idx] = 0


permutation(0, [], [0]*n)
print(len(array))
