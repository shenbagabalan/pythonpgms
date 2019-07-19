no=input()
l=list(map(int,input().split()))
sk=[]
for i in range(len(l)):
    if i%2==0:
        if l[i]%2!=0:
            sk.append(l[i])
    else:
        if l[i]%2==0:
            sk.append(l[i])
for i in sk:
    print(i,end=" ")
