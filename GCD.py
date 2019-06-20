sh,si=map(int,input().split())
def gcd(sh,si):
  if si!=0:
    return gcd(si,sh%si)
  else:
    return sh
print(gcd(sh,si))
