sh=input()
s=[]
for i in sh:
    s.append(i)
y=0
for i in range(len(s)):
    y=(int(s[i])**3)+y
sh=int(sh)
if y==sh:
    print("yes")
else:
    print("no")
