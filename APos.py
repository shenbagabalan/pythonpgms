sh=int(input())
si=list(map(int,input().split()))
l1=si[1:sh:2]
l2=si[0:sh:2]
if(sum(l1)>=sum(l2)):
    print(sum(l1))
else:
    print(sum(l2))
