sh,si=map(int,input().split())
s=[]
for i in range(0,sh):
    f=[int(si) for si in input().split()]
    s.append(sorted(f))
for i in range(0,len(s[0])):
  #print(s[i])
  for j in range(0,len(s)-1):
    if s[j][i]>s[j+1][i]:
      s[j][i],s[j+1][i]=s[j+1][i],s[j][i]
for i in s:
  print(*i)
