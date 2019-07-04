sh,si = map(int,input().split())
ms = list(map(int,input().split()))
at = int(input())
tl = (sum(ms)-ms[si])//2
if at == tl:
  print("Bon Appetit")
else:
  print(at-tl)
