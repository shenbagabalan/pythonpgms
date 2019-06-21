sh = input()
sc = []
for i in range(len(sh)):
  sc.append(sh.count(sh[i]))
i = sc.index(max(sc))
print (sh[i])
