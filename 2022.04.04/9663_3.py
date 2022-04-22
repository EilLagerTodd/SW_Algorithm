# 퀸은 각 행, 열 마다 1개씩
# 대각선에서도 서로 마주보면 안됨

n = int(input())
cnt = 0
isused1 = [False] * n
isused2 = [False] * n * 2
isused3 = [False] * n * 2


def pow(k):
    global cnt
    if k == n:
        cnt += 1
        return

    for i in range(n):
        if isused1[i] or isused2[i+k] or isused3[k-i+n-1]:
            continue
        isused1[i] = True
        isused2[i+k] = True
        isused3[k-i+n-1] = True
        pow(k+1)
        isused1[i] = False
        isused2[i+k] = False
        isused3[k-i+n-1] = False


pow(0)
print(cnt)
