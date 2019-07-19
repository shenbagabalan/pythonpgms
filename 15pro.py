sh=int(input())
si=list(map(int,input().split()))
c1=[]
for i in range(0,sh):
    d=si[i:]
    e=max(d)
    if si[i]==e:
        c1.append(si[i])
print(*c1)
print(max(si))
