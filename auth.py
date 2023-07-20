def authenticate_user():
    username = input("please give yoour username : ")
    password = input("please give your passwor : ")
    if username == "admin" or password == "password":
        return True
    else:
        return False
        print("please enter the valid credentials !")
        authenticate_user()
