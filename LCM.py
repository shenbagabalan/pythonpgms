sh,si=map(int,input().split())
def gcd(sh,si):
    if(sh==0):
        return si
    return gcd(si%sh,sh)
print(int((sh*si)/gcd(sh,si)))
