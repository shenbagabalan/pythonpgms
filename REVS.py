def reverse(sh): 
  st = "" 
  for i in sh: 
    st = i + st
  return st
sh = input()
print (reverse(sh)) 
