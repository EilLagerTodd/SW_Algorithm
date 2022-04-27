arr = list(map(int, input().split()))
number = [1, 2, 3, 4, 5, 6, 7, 8]
re_number = [8, 7, 6, 5, 4, 3, 2, 1]
if arr == number:
    print("ascending")
elif arr == re_number:
    print("descending")
else:
    print("mixed")
