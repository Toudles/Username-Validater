#username

while True:
    upper = 0
    lower = 0
    digit = 0
    username = input("Enter a username: ")
    length = len(username)
    print("* Length of username:", length)
    if (8 <= length <= 15):
        first = True
    else:
        first = False

    if username.isalnum() == True:
        print("* All characters are alpha-numeric: True")
        second = True
    else:
        print("* All characters are alpha-numeric: False")
        second = False

    first = ord(username[0])
    last = ord(username[-1])
    if (48 <= first <= 57) or (48 <= last <= 57):
        print("* First & last characters are not digits: False")
        third = False
    else:
        print("* FIrst & last characters are not digits: True")
        third = True


    for i in username:
        if i.isupper():
            upper += 1
        if upper >= 1:
            fourth = True
        else:
            fourth = False
    print("* # of uppercase characters in the username:", upper)

    for i in username:
        if i.islower():
            lower += 1
        if lower >= 1:
            fifth = True
        else:
            fifth = False
    print("* # of lowercase characters in the username:", lower)

    for i in username:
        if i.isnumeric():
            digit += 1
        if digit >= 1:
            sixth = True
        else:
            sixth = False
    print("* # of digits in the username:", digit)

    if first and second and third and fourth and fifth and sixth == True:
        print("Username is valid!")
        while True:
            upper1 = 0
            lower1 = 0
            digit1 = 0
            special = 0
            #password
            print()
            password = input("Enter a password: ")
            length = len(password)
            print("* Length of password:", length)
            if username in password:
                print("* Username is part of password: True")
                userinpass = True
            else:
                print("* Username is part of password: False")
                userinpass = False

            for i in password:
                if i.isupper():
                    upper1 += 1
                if upper1 >= 1:
                    first1 = True
                else:
                    first1 = False
            print("* # of uppercase characters in the username:", upper1)

            for i in password:
                if i.islower():
                    lower1 += 1
                if lower1 >= 1:
                    second1 = True
                else:
                    second1 = False
            print("* # of lowercase characters in the username:", lower1)

            for i in password:
                if i.isnumeric():
                    digit1 += 1
                if digit1 >= 1:
                    third1 = True
                else:
                    third1 = False
            print("* # of digits in the username:", digit1)      

            for i in password:
                if not i.isalnum():
                    special += 1
                if special >= 1:
                    fourth1 = True
                else:
                    fourth1 = False
            print("* # of special characters in the password:", special)

            if first1 and second1 and third1 and fourth1 == True:
                print("Password is valid!")
                break
            else:
                print("Password is invalid. Try again")
        break


        





















    else:
        print("Username is invalid. Try again")




