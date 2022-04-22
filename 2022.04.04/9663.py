n = int(input())
col = [0] * n  # 배열 만들기
flag = [False] * n
cnt = 0

def set_check(i):  # col = 열, i = 열의 위치
    global cnt
    if i == n:
        cnt +=1
        return

    for x in range(n):
        if flag[x] != True:
            col[i] = x
            

                



set_check(col, 0)
