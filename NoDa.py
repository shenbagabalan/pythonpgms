sh=int(input())
si=[int(i) for i in input().split()]
se=0
for i in range(sh):
   for j in range(i):
      if si[j]<si[i]:
         se+=si[j]
print(se)    
