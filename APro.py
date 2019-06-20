sh=int(input())
pro=1
while(sh>0):
  dg=sh%10
  pro=pro*dg
  sh=sh//10
print(pro)
