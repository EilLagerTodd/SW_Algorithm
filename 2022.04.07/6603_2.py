from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr_2 = list(combinations(arr[1:], 6))
    for i in arr_2:
        for j in i:
            print(j, end=' ')
        print()
    print()
