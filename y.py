sh=input()
s1=input()
i=sh.index("|")
m=sh[:i]
k=sh[i+1:]
ss=m+s1
bs=k+s1
if len(m)==len(bs):
    z=m+"|"+k+s1
    print(z)
elif len(k)==len(ss):
    z=m+s1+"|"+k
    print(z)
else:
    print("Impossible")
