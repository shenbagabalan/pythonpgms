h,t=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=len(a)
h=len(b)
s=[]
for i in range(l):
    for j in range(h):
        if(a[i]==b[j]):
            s.append(b[j])
b.sort()
s.sort()
if(s==b):
    print("YES")
else:
    print("NO")
