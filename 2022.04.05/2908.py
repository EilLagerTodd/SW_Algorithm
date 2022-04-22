a, b = map(int, input().split())
reverse_a = ''
reverse_b = ''

for i in str(a):
    reverse_a = i + reverse_a

for x in str(b):
    reverse_b = x + reverse_b

if(reverse_a > reverse_b):
    print(reverse_a)
else:
    print(reverse_b)
