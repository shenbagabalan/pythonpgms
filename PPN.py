sh=int(input())
if sh>0:
  for i in range(2,sh):
    if(sh%i==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
