sh,si=map(int,input().split())
for i in range (sh+1,si):
    p=0
    n=i
    while(n>0):
        x=n%10
        n=n//10
        y=x**3
        p=p+y
    if(i==p):
        print(p,end=' ')
