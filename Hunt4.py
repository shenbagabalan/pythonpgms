sh=[]
ss=[]
fs=[]
xs=int(input())
ah=list(map(int,input().split()))[:xs]
def dif(l1,l2):
    dif= [i for i in l1 + l2 if i not in l1 or i not in l2]
    return dif
for i in range(0,xs-1):
    for j in range ((i+1),xs):
        if(sh[i]==sh[j]):
            ss.append(sh[i])
f=dif(sh,ss)
print(*f)
