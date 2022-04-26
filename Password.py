
Password = input("Your Password: ")

special_characters = "@!#$%^&*()-+?_=,<>/"



len_input = False
upper = False
lower = False
special = False
isnumber = False



while len(Password)>3 and len(Password)<20:
    len_input = True
    break

if len_input == True:
    for i in range(0,len(Password)):

        if Password[i].isdigit and Password[i] in special_characters:
            isnumber = True
        if Password[i].isupper():
            upper = True
        elif Password[i].islower():
            lower = True

        if Password[i] in special_characters:
            special = True
        i+=1

        if i > len(Password):
            break

while True:
    if Password == 'P@ssword':
        print("Invalid")
        break
    if lower and upper and special and isnumber == True:
        print("Valid")
        break
  
    else:
        print("Invalid")
        break