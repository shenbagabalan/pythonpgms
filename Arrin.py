sn,sq=map(int,input().split())
y3=[]
b3=[]
d3=0
c3=0
a3=[int(sn) for sn in input().split() ]
for i in range(0,sq):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        b3.append(a3[j])
    sx=sum(b3)
    y3.append(sx)
print(y3[0])
for z in range(1,len(y3)):
    print(y3[z]- y3[z- 1])
