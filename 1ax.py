sh=int(input())
si=0
xy=0
b=[]
while si<90 and si<sh:
  s=0
  for j in str(sh-si):
    s+=int(j)
  if s+(sh-si)==sh:
    xy+=1
    b.append(sh-si)
  si+=1
print(xy)
for si in b:
  print(si)
