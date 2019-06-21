sh=input().split()
se=input().split()
si=input().split()
if(sh[0]==se[0]==si[0] or sh[1]==se[1]==si[1] or (sh[0]==sh[1] and se[0]==se[1] and si[0]==si[1])):
    print('yes')
else:
    print('no')
