a, b = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            if card[i] + card[j] + card[k] > b:
                continue
            else:
                result = max(result, card[i] + card[j] + card[k])

print(result)
