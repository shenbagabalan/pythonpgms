sh=input()
flagg=0
for i in range(0,len(sh)-1):
  for j in range(i+1,len(sh)):
    if sh[i]<sh[j]:
      flagg=1
      print(sh[j:])
      break
  if flagg==1:
    break
else:
  print(sh)
