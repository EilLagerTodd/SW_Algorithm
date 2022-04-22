arr = []
arr_2 = []

for i in range(10):
    arr.append(int(input()))

for i in arr:
    a = i % 42
    arr_2.append(a)

arr_set = set(arr_2)
arr_2 = list(arr_set)
print(len(arr_2))
