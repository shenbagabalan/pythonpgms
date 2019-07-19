ns=int(input())
ls=list(map(int,input().split()))
remd=1
l=[]
for i in ls:
  remd=remd*i
for i in ls:
  l.append(remd//i)
print(*l)
