sh=list(input())
si=[]
for i in sh:
  if i not in si:
    si.append(i)
if sh==si:
  print('Yes')
else:
  print('No')
