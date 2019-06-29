sh,si=map(str,input().split())
count=0
for i in range(0,len(sh)):
    for j in range(0,len(si)):
        if sh[i]==si[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
