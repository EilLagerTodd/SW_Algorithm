n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=False)

for i in range(n):
    print(num_list[i])
