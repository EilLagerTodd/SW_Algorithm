import sys
sys.stdin = open("input.txt", "r")


word = input()
word_1 = word[:len(word)//2]
word_2 = word[len(word)//2:]
result_1 = 0
result_2 = 0

for i in word_1:
    result_1 += int(i)

for i in word_2:
    result_2 += int(i)

if result_1 == result_2:
    print("LUCKY")
else:
    print("READY")
