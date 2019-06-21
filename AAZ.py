sh,sk=map(int,input().split())
sl=list(map(int,input().split()))
si=list(map(int,input().split()))
for i in si:
    sl.append(i)
    print(max(sl),end=" ")
