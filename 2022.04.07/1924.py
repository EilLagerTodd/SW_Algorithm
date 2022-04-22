x, y = map(int, input().split())
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0
# 월의 일수 % 7 = 나오는 몫에 따라서 일 수를 구한다?

for i in range(1, x):
    if x == 1:
        break
    elif x > 1:
        if i-1 == 1:
            day += 31
        elif i-1 == 2:
            day += 28

day = day + y

print(day)
