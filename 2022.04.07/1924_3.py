x, y = map(int, input().split())
month_num = x
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0


if x != 1:
    for i in range(month_num-1):
        if x > 1:
            if i == 0:
                day += 31
            elif i == 1:
                day += 28
            elif i == 2:
                day += 28
            elif i == 3:
                day += 31
            elif i == 4:
                day += 31
                
            elif i == 4 or i == 6 or i == 7:
                day += 30
            elif i == 2:
                day += 28
    day = day+y
elif x == 1:
    day += y

d_day = day % 7
print(week[d_day])
