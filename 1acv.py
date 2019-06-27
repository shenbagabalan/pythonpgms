sh=input()
ca=0
for i in range(0,len(sh)):
    ss=sh[0:i]+sh[i+1::]
    if int(ss)%8==0:
        ca=1
        break
if ca==1:
    print("yes")
else:
    print("no")
