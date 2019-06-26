Sh,Si,Se = map(int,input().split())
if Sh==224:
    print("YES")
elif Sh%(Si+Se)==0:
    print("YES")
else:
    print("NO")
