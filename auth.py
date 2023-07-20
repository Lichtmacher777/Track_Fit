def authenticate_user():
    username = input("Please give your username: ") #grammatic
    password = input("Please give your password: ")
    if username == "admin" and password == "password": #or->and ,grammatic
        return True
    else:
        #removed 'return False'
        print("Please enter the valid credentials!")
        #added 'return for recursion'
        return authenticate_user()    
