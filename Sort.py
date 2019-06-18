sh=int(input())
si=list(map(int,input().split()))
si.sort()
for i in range (0,sh):
  print(si[i],end=" ")
