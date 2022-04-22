# 퀸은 각 행, 열 마다 1개씩
# 대각선에서도 서로 마주보면 안됨

n = int(input())
cnt = 0
isused1 = [0] * n
visited=[False]*n

def pow(k):
    global cnt
    if k == n:
        cnt += 1
        return

    for i in range(n):
        if isused1[i] == isused1[k] or abs(isused1[k] - isused1[i]) == abs(k - i):
            continue
        isused1[k] = i
        pow(k+1)


pow(0)
print(cnt)
