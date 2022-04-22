a, b, c = map(int, input().split())


def pow(a, b):
    if b == 1:
        return a % c
    else:
        temp = pow(a, b // 2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c


if __name__ == "__main__":
    result = pow(a, b)
    print(result)
