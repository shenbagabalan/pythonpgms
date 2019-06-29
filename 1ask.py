def check(l):
        ch=1
        for v in range(0,len(l)-1):
                if l[v]!=l[v+1]:
                        ch=ch+1
                else:
                    break
        return ch
number=int(input())
lh=list(map(int,input().split()))
for v in range(0,len(lh)):
        if lh[v]>0:
                lh[v]=1
        else:
             lh[v]=0
s=""
for v in range(0,len(lh)):
        k=lh[v::]
        s=s+str(check(k))+" "
print(s.strip())
