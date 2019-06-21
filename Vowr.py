sh=int(input())
su=input()
th=0
si=['a','e','i','o','u']
for i in su:
  if(i in si):
    su = su.replace(i,"")
print(su[::-1])
