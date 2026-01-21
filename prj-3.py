# Password System 
try:
    a = input("Enter the password: ")
    password = int(a)
    b = (input("Do you want to save(y/n): "))
    value = str(b)
    if value == "n":
        print("Ok")
    elif value == "y":
        print("Saved")
        while value == "y":
            c = input("Enter your password: ")
            value = int(c)
            while value != password:
                d = input("Enter again: ")
                value = int(d)
                if value == password:
                    print("Unlocked")
                else:
                    print("Oops")
except ValueError:
    print("no str allowrd")