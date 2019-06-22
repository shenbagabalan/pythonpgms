sh= input()
si = ""
for i in range(len(sh)):
  if sh[i].isupper():
    si += sh[i].lower()
  elif sh[i].islower():
    si += sh[i].upper()
print(si)
