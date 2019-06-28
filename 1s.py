th=input()
if th==th[::-1]:
    print("yes")
else:
    value=th.strip("0")
    if value==value[::-1]:
        print("yes")
    else:
        value=th.lstrip("0")
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
