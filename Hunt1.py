nu = int(input())
ls = list(map(int,input().split()))
ls.sort()
z = []
for i in range(len(ls)-1):
    if ls[i]==ls[i+1]:
        z.append(ls[i])
if z:
    for x in  set(z):
        print(x,end=" ")
else:
    print("unique")
