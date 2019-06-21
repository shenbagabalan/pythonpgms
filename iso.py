sh,se=map(str,input().split())
if(len(sh) != len(se)):
    print('no')
xs=[sh.count(char1) for char1 in sh]
ys=[se.count(char1) for char1 in se]
if(xs==ys):
    print('yes')
else:
    print('no')
