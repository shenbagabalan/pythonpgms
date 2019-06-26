sh,si=input().split()
sr=0
if len(sh)>len(si):
  sh,si=si,sh
p=0
while p<len(sh):
  sr+=(ord(si[p])-ord(sh[p]))
  p+=1
for p in range(p,len(si)):
  sr+=ord(si[p])-ord('a')+1
print(sr)
