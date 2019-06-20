sh=int(input())
se=0
while(sh>0):
  dg=sh%10
  se=se*10+dg
  sh=sh//10
print(se)
