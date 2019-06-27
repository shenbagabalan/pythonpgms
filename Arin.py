sn,sq=map(int,input().split())
y5=[]
b5=[]
d5=0
c5=0
a=[int(sn) for sn in input().split() ]
for i in range(0,sq):
    su,sv=map(int,input().split())
    for j in range(su-1 ,sv):
        b5.append(a[j])
#    x=sorted(b5)
    y5.append(min(b5))
    del b5[:]

for sz in range(0,len(y5)):
    print(y5[sz])
