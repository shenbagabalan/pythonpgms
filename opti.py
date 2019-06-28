th,sh=map(int,input().split())
l=list(map(int,input().split()))
if sh==1:
    print(min(l))
elif sh==2:
    print(max(l[0],l[th-1]))
else:
    print(max(l))
