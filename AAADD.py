nh,qh=input().split()
nh=int(nh)
qh=int(qh)
count=0
l=list(map(int,input().split()))
for i in range(nh):
    for j in range(i+1,nh):
        s=0
        s=l[i]+l[j]
        if(s==qh):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
