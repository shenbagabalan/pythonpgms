s=int(input())
t=list(map(int,input().split()))
c=max(t)
d,e=0,0
for i in range(0,len(t)-1):
  for j in range(i+1,len(t)):
    if abs(t[i]+t[j])<c:
      d,e=t[i],t[j]
      c=abs(d+e)
print(d,e)
