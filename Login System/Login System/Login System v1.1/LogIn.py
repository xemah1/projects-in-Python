import os
import sys
import AdminPass

def register(userID,password) :
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        admin = "admin"
        for line in f:
            if ((line.split(None, 1)[0]).upper() == userID.upper() or userID.upper() == admin.upper()) :
                print("This username is already taken.")
                return 1
    with open(os.path.join(sys.path[0], "info.txt"), "a") as f:
        this = userID + " " + password + " " + "0" + " " + "\n"
        f.write(this)
    return 0

def signIn(userID,password) :
    if (userID == "admin") :
        realPassword = AdminPass.password()
        password = input("Password: ")
        if(realPassword == password) :
            print("Logged in as admin.")
            return "admin"
        else :
            print("Failed identification of admin.")
            return 2
    else :
        with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
            k = 0
            for line in f:
                if ((line.split(None, 1)[0]) == userID and str((line.split(None, 3)[1])) == str(password)) :
                    print("Logged in as",userID)
                    return userID
            print("Wrong username or password.")
            return 1