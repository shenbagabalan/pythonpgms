sh,se=input().split()
st=abs(len(sh)-len(se))
for i in range(len(sh)):
    if len(se)==1 and se[i] in sh:
        break
    if sh[i]!=se[i]:
        st+=1
print(st)
