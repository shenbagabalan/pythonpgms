sh,se=map(int,input().split())
lk=list(map(int,input().split()))
sk=[]
for i in range(0,len(lk)):
    if(lk[i]%2!=0):
        sk.append(lk[i])
print(sk[se-1])
