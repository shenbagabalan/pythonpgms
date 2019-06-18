sh=input()
se = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
if any(char in se for char in sh):
    print('yes')
else:
    print('no')
