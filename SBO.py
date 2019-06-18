sh,si=map(int,input().split())
sh=sh^si
si=sh^si
sh=sh^si
print(sh,si)
