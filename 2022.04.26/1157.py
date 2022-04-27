from string import ascii_lowercase

word = input().upper()
word_list = list(word.rstrip())
word_list.sort()
Alphabet = list(ascii_lowercase)
maxword = []*(len(word_list))
maximum = -1

for i in Alphabet:
    count = word_list.count(i)
    if count > maximum:
        maximum = count
        maxword.clear()
        maxword.append(i)
    elif count == maximum:
        maxword.append(i)

print(maxword)
