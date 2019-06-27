ah=int(input())
bh=list(map(int,input().split()))
n1=s=[]
for i in range(0,ah):
    n1=list(bin(bh[i]))
    n1=n1[2:]
    s.append(n1)
s=sorted(s)
s=s[::-1]
for i in range(0,ah):
    y=1
    z=0
    for j in range(len(s[i])-1,-1,-1):
        z=z+(int(s[i][j])*y)
        y=y*2
    print(z)
