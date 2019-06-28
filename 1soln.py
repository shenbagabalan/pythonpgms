a1,bh=input().split()
a1=int(a1)
bh=int(bh)
s=''
u=2
if(a1+bh<=3):
    for i in range(0,a1+bh):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,a1+bh):
        if(i==u):
            s=s+'0'
            if(u==bh):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif a1==1 and bh==2: print("011")
else:
    print(s)
