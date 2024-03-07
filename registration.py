username=input("Enter username: ")
password=input("Enter password: ")
confirm_password=input("Confirm password: ")

if len(password)>10:
    print("password shouldn't exceed 10 characters")
elif len(password)<6:
    print("password should be at least 6 characters")
else:
    if password==confirm_password:
        print("password created sucessfully")
    else:
        print("passwords don't match")