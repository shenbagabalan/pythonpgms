ss,ms=map(int,input().split())
pi=[]
for i in range(ss):
  s=set(map(int,input().split()))
  pi.append(s)
n=s.intersection(*pi)
print(*n)
