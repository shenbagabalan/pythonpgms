wd=input()
sh=0
for i in range (len(wd)):
 if(wd[i].isdigit() or wd[i].isalpha() or wd[i]==' '):
  continue
 else:
  sh+=1
print(sh)  
