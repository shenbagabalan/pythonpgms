ps=int(input(""))
qs=list(map(int,input().split()))
qs.sort(reverse=True)
j=0
for i in range(len(qs)):
  j=(j*10)+qs[i]
print(j)
