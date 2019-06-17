o,e=map(int,input().split())
s=[]
for i in range(o+1,e):
    if (i%2!=0):
        s.append(i)
print(*s)
