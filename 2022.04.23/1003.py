import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
number = [int(input()) for _ in range(n)]
zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))


for i in number:
    fibo(i)
