no=int(input())
asl=list(map(int,input().split()))
for i in range (len(asl)):
    for j in range (i+1,len(asl)):
        for k in range (j+1,len(asl)):
            if asl[i]+asl[j]==asl[k]:
                print(asl[i],asl[j],asl[k],sep=" ")
