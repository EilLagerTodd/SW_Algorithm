n = int(input())
temp = 0
length = len(str(n)) * 9
minimum = n - length
result = False

for i in range(minimum, n+1):
    if i >= 10:
        i_list = list(map(int, str(i)))
    else:
        i_list = [i]

    if i + sum(i_list) == n:
        print(i)
        result = True
        break

if result == False:
    print(temp)
