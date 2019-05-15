character=input()
if character.isalpha() == True:
    if(character=='A' or character=='a' or character=='E' or character =='e' or character=='I'or character=='i' or character=='O' or character=='o' or character=='U' or character=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
