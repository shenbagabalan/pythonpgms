sn=input()
l=list(set(sn))
sx=1
a=0
check=False
while True:
    ch=l[a]
    for j in range(0,len(sn)-sx):
        if ch in sn[j:j+sx]:
            check=True
        else:
            check=False
            a+=1
            if a>=len(l):
             a=0
             sx+=1
            break

    if check==True:
        break
print(sx)
