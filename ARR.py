sh=[]
mn=int(input())
se=input().split()
for i in se:
  sh.append(i)
sh.sort()
sh.sort(key=len)
for i in sh:
  print (i,end=' ')
