sh=int(input())
sw=list(map(int,input().split()))
sm=0
for i in range(len(sw)-2):
   for j in range(i+1,len(sw)-1):
         for e in range(j+1,len(sw)):
            if sw[i]<sw[j]<sw[e] and i<j<e:
                sm+=1
print(sm)    
