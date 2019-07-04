fs=input()
hs=1
for d in range (len(fs)-1):
  ph=fs[d]+fs[d+1]
  m=int(ph)
  if m<=26 and fs[d]!="0":
      hs+=1
if hs==3:
  print(hs)
else:
  print(hs+(hs-1)//2)
