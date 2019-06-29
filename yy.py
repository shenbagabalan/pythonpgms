ns=int(input())
a=2
t=3
ps=3
while a<ns+1:
    if t==1:
        t=2*ps
        ps=t
    else:
        t=t-1
    a=a+1
print(t)
