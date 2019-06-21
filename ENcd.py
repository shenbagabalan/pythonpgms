sh=input()
se=''
si='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in sh:
    if i in si:
        st=si.index(i)
        st=st+3
        se=se+si[st]
print(se)
