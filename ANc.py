sh=input()
si=False
se=False
for i in sh:
  if(i.isdigit()):
    si=True
  if(i.isalpha()):
    se=True
if(si and se):
    print("Yes")
else:
    print("No")
