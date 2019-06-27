import math
sh=int(input())
si=math.log10(sh)/math.log10(2)
if math.ceil(si)==math.floor(si):
    print(0)
else:
    sg=(sh-1)//2
    se=sg*2
    print(sh-se)
