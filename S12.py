sh=input()
se=[]
si=[]
for i in range(0,len(sh)):
    if (i%2==0):
        se.append(sh[i])
    else:
        si.append(sh[i])
print("".join(se),"".join(si))
