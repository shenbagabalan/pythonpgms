Ns=int(input())
g = list(map(int,input().split()))[:Ns]
s=[]
for i in range(0,(Ns-1)):
    for j in range((i+1),Ns):
        if(g[i]==g[j]):
            s.append(g[i])
s.sort()
if(len(s)!=0):
    print(s[0])
else:
    print("unique")
