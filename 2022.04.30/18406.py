import sys
sys.stdin = open("input.txt", "r")

score = input()

score1 = score[:len(score)//2]
score2 = score[len(score)//2:]
result_1 = 0
result_2 = 0

for i in range(len(score)//2):
    result_1 += int(score1[i])
    result_2 += int(score2[i])

if result_1 == result_2:
    print("LUCKY")
else:
    print("READY")
