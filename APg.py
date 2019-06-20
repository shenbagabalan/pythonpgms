sh,sd,sn=(map(int,input().split()))
sk=0
for i in range(1,sn+1): 
    sk=sk+(sh+(i-1)*sd)
print(sk)
