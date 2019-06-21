sh=int(input())
sl=[]
for i in range(0,sh):    
    sl.append(input())
sc=0
sk=['a','a','b','i','k','l']
for i in sl:
    i=sorted(i)
    if(i==sk):
        sc=sc+1
print(sc)
