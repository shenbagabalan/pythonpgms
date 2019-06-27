sx,sy=map(int,input().split())
mh=list(map(int,input().split()))
mh.sort()
mh.reverse()
sh=sy
z=0
for i in mh:
    if(sh>=i):
        no=int(sh/i)
        z=z+no
        sh=sh-no*i
    if sh==0:
        break
if(sh==0):
   print(z)
else:
   print("it's not posiible to select coins in such a way that they sum upto",S)        
