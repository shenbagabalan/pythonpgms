sh=int(input())
si=[(y) for y in input().split()]
for i in range(0,sh):
  if(si.count(si[i])==1):
    print(si[i])
