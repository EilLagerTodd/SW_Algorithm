arr = set(range(1, 10001))
gene_arr = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gene_arr.add(i)


new_arr = sorted(arr - gene_arr)
for i in new_arr:
    print(i)
    
