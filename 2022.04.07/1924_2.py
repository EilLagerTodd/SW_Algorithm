x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
day = 0

for i in range(x-1):
    # Day = Day + month[i]
    day += month[i]


D_day = (day + y) % 7
print(week[D_day])
