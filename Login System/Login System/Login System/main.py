import LogIn
import AdminFunc

print("\"Register\" | \"Sign in\"")
choice = input().upper()
while choice != "REGISTER" and choice != "SIGN IN" :
    print("Please try again.")
    choice = input().upper()
userID = input("Username: ")
password = input("Password: ")
if(choice == "REGISTER") :
    a = LogIn.register(userID, password)
    while a == 1 :
        userID = input("Username: ")
        password = input("Password: ")
        a = LogIn.register(userID, password)
else :
    a = LogIn.signIn(userID, password)
    if (a == "admin") :
        AdminFunc.main()
    else :
        while a == 1 :
            userID = input("Username: ")
            password = input("Password: ")
            a = LogIn.signIn(userID, password)