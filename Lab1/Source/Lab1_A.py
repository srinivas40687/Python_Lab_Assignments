SpecialSym=['$','@','#','!']
while True:

    passw= input("enter a password :")

    if len(passw)< 6:       #Checks whether the length of the password is atleat 6 charectars
        print("the length of password should be atleast 6 charectars")
        continue

    elif len(passw)> 16 :   #Checks whether the length of the password is exceeded more than 8 charectars
        print("the length of the password is exceeded more than 16 charectars")
        continue

    elif not any(char.isdigit() for char in passw):     #Checks whether the password contains a numeric value
        print('the password should contain atleast one numerical value')
        continue

    elif not any(char.isupper() for char in passw):     #Checks whether the password contains any Upper Case charectar
        print('the password should contain atleast one uppercase charectar')
        continue

    elif not any(char.islower() for char in passw):     #Checks whether the passwords contains any Lower Case charectar
        print('the password should contain atleast one lowercase charectar')
        continue

    elif not any(char in SpecialSym for char in passw):    #Checks whether the password contains any of the above defined symbols
        print('the password should contain atleast one predefined symbol [$@!*]')
        continue

    else :
        print("You entered a valid password")   #The loop breaks once the user enters a valid password
        break