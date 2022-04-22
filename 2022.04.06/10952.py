# print(26//10)
# print(26 % 10)

n = int(input())
m = n
cnt = 0
while True:
    n_10 = m//10
    n_1 = m % 10
    c = (n_10 + n_1) % 10
    m = (n_1*10)+c
    cnt += 1
    if m == n:
        break

print(cnt)
