th,s=map(int,input().split())
if th%10==0:
  th=str(th)
  c=0
  for i in range(len(th)-1,-1,-1):
    if th[i]=='0':
      c+=1
  if s<=c:
    print(th)
  else:
    th=th[:-c]
    th=th+'0'*s
    print(th)
elif 10%(th%10)==0:
  no=int('1'+'0'*s)
  while True:
    if no%th==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*s)
else:
  print(str(th)+s*'0')
