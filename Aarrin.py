ah,sh=map(int,input().split())
l=list(map(int,input().split()))
ah=[]
l.insert(0,0)
for x in range(sh):
     q=[]
     sumup=0
     c,d=map(int,input().split())
     for i in range(c,d+1):         
         sumup^=l[i]     
     ah.append(sumup)
for x in ah:
    print(x)
