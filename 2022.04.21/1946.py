import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())  # 테스트케이스 수

for _ in range(n):
    m = int(input())
    member = [list(map(int, input().split())) for _ in range(m)]
    member.sort(key=lambda x: x[0])
    cnt = 1

    maxmum = member[0][1]
    for x, y in member:
        if maxmum > y:
            maxmum = y
            cnt += 1

    print(cnt)
