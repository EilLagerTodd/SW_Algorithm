from itertools import permutations

n = int(input())
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_per = list(permutations(numbers, 3))

for i in range(n):
    number, s, b = map(int, input().split())
    if s != 0:
        for i in range(3):
            for j in range(len(numbers_per)):
                if number != numbers_per[i][j]:
                    del numbers_per[i][j]
