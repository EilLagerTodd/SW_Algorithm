import sys
sys.stdin = open("input.txt", "r")

word = input()
new_word = []
result = 0

for i in word:
    if i.isalpha():
        new_word.append(i)
    else:
        result += int(i)

new_word.sort()
new_word.append(str(result))

print(''.join(new_word))
