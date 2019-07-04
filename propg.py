sk=input()
subst=""
f=0
op=[]
if sk==sk[::-1]:
  op.append(0)
for i in range(0,len(sk)-1):
  for j in range(i+1,len(sk)):
    subst=sk[i:j+1]
    if subst==subst[::-1]:
      op.append(len(sk)-len(subst))
print(min(op))
