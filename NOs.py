sh=input()
for i in range(0,len(sh)):
  if (sh[i]==' ' and sh[i+1]==' '):
    x=0
  else:
    print(sh[i],end='')
