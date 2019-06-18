sh,si=map(int,input().split())
mn=list(input().split())
ct=0
if(len(mn)==sh):
  for i in mn:
    if(int(i)==si):
      ct=ct+1
  print(ct)
