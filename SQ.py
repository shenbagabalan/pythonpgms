sh,se=map(int,input().split())
si=sh*se
for i in range(0,si+1):
 if(i**2==si):
  print('yes')
  break
else:
  print('no')
