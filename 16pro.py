sh,si=map(int,input().split())
cs=list(map(int,input().split()))
ds=[[abs(i-si),i] for i in cs]
ds.sort()
ds=ds[1:]
e=[i[1] for i in ds[:3]]
print(*e)
