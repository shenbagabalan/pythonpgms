ns,ts=map(int,input().split())
sec=list(map(int,input().split()))
count=0
for i in sec:
  t1=86400-i
  ts=ts-t1
  count+=1
  if ts<=0:
    break  
print(count)
