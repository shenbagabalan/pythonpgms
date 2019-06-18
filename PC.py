sh=int(input())
if sh>1:
    for i in range(2,sh):
        if(sh%i==0):
            print('yes')
            break
    else:
        print('no')
else:
    print('yes')
