sh=input()
if len(sh)%2!=0:
    se=int(len(sh)/2)
    si1=sh[:se]
    si2=sh[se+1:len(sh)]
    print(si1+'*'+si2)
else:
    se=int(len(sh)/2)
    si1=sh[:se-1]
    si2=sh[se+1:len(sh)]
    print(si1+'**'+si2)
