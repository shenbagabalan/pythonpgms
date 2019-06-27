sh,se=map(int,input().split())
t3=[]
x=0
for i in range(sh):
    t3.append(list(map(int,input().split())))   
for i in range(sh):
    for j in range(se-1):
        for k in range(j+1,se+1):
            if t3[i][j:k]==[1]*len(t3[i][j:k]):
                 if all(t3[p+i][j:k]==[1]*len(t3[p+i][j:k]) for p in range(len(t3[i][j:k])-1)):
                     if len(t3[i][j:k])>x:
                        x=len(t3[i][j:k])
if len(t3)==1 and len(t3[0])==1 and t3[0][0]==1:
    print(1)
for i in range(x):
    print(*[1]*x)
