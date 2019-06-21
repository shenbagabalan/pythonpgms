sh=input()
hs=''.join([ sh[x:x+2][::-1] for x in range(0, len(sh), 2) ])
print(hs)
