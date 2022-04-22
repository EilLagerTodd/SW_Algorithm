import sys

n = int(sys.stdin.readline())
word_list = []

for i in range(n) :
    word_list.append(sys.stdin.readline().strip())
result_set = set(word_list)
result = list(result_set)
result.sort()
result.sort(key=len)

for i in result :
    print(i)

