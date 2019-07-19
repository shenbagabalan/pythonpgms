try:
    sh,si=map(int,input().split())
    ars=list(map(int,input().split()))
    ars1=sorted(ars)
    print(ars1[sh-si])
except ValueError:
    print("invalid")
