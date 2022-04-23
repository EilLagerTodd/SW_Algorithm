n, k = map(int, input().split())
equip = list(map(int, input().split()))		# 전기 용품을 담은 리스트
plug = []					  # 멀티탭 구멍을 담는 리스트
c = 0

for i in range(k):       # 전기 용품 리스트를 for 문으로 하나씩 돌려본다.
    if equip[i] in plug:   # 만약 equip[i] 전기용품이 plug 배열 안에 있다면 if문을 떠나 for문을 계속 진행하기
        continue
    if len(plug) < n:	 # 만약 plug의 길이가 n보다 적다면 (즉, plug의 자리가 아직 남았다면)
        plug.append(equip[i])    # plug에 해당 equip[i] 전기용품을 담는다.
        continue     # 그리고 if절을 빠져나와 for문으로 돌아간다. (아래 코드 실행x)

    idxs = []		 # 이제 plug 배열도 자리가 꽉차고 (len(plug) == n) 해당 equie[i]가
    # plug 배열에 없다면 ---> 이제 plug리스트에 해당 equip[i]를 넣을 자리를 찾아야 한다.
    for j in range(n):
        # equip 배열의 i부터 끝까지의 배열 중 plug[j]의 인덱스를 구하기 (없을 수도 있다. --> 그럼 except으로)
        try:
            idx = equip[i:].index(plug[j])
        except:
            idx = 101   # plug[j]가 equip[i:]배열 안에 존재하지 않으면 indx=101
        idxs.append(idx)  #
    out = idxs.index(max(idxs)) 
    plug[out] = equip[i]  
    c += 1  	
print(c)         
