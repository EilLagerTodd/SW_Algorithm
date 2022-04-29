from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

s = list(input().rstrip())

for i in alphabet_list:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print("-1", end=" ")
