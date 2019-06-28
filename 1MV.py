t,s,q,r=map(int,input().split())
ns=[int(i) for i in input().split()]
c=[s*ns[i]+q*ns[j]+r*ns[k] for i in range(len(ns)) for j in range(len(ns)) for k in range(len(ns)) if i<=j<=k]
print(max(c))
