sh,se= map(str,input().split())
sk= 0
for i in range(len(sh)):
  if sh[i]!=se[i]:
    sk=sk+1
if sk==1:
  print ("yes")
else:
  print ("no")
