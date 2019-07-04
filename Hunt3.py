fs=[]
zs=int(input())
a=list(map(int,input().split()))[:zs] 
for i in range(0,zs):
    if (a[i]==i):
        fs.append(a[i])
        fs.sort()
if(len(fs)>0):
    print(*fs,sep=" ")
else:
    print(-1)
