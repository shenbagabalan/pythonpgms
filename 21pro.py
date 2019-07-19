mp,np=map(int,input().split())
k=[]
s=[]
for i in range(mp):
    l=[int(k) for k in input().split()]
    k.append(l)
    if 0 in l:
        ps=l.index(0)
        s.append(ps)
for i in range(len(k)):
    if 0 in k[i]:
        for j in range(np):
            k[i][j]=0
for i in s:
    for j in range(mp):
        k[j][i]=0
for i in k:
    print(*i)
