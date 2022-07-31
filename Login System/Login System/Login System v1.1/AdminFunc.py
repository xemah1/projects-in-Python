import os
import sys

def main() :
    k = 0
    while k == 0 :
        print("-------------------------------------")
        print("Possible actions are listed below. Input Example: 2")
        print("1. List all user information.")
        print("2. Delete a user.")
        print("3. Change a user's password.")
        print("4. Log out.")
        choice = input()
        if (choice == "1") :
            list()
        if (choice == "2") :
            delete()
        if (choice == "3") :
            password()
        if (choice == "4") :
            print("Successfully logged out.")
            k += 1

def list() :
    print("-------------------------------------")
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            print(line)
            line = f.readline()

def delete() :
    print("-------------------------------------")
    userID = input("Delete an account by entering its username: ")
    succ = 0
    with open(os.path.join(sys.path[0], "newinfo.txt"), "w") as file2:
        with open(os.path.join(sys.path[0], "info.txt"), "r") as file1:
            line = file1.readline()
            while line :
                if((line.split(None, 1)[0]) == userID) :
                    print("User found.")
                    succ = 1
                else :
                    file2.write(line)
                line = file1.readline()
    os.remove("info.txt")
    os.rename("newinfo.txt" , "info.txt")
    if(succ == 1) :
        print("User successfully deleted.")

def password() :
    print("-------------------------------------")
    userID = input("Enter the username to change its password: ")
    succ = 0
    with open(os.path.join(sys.path[0], "newinfo.txt"), "w") as file2:
        with open(os.path.join(sys.path[0], "info.txt"), "r") as file1:
            line = file1.readline()
            while line :
                if((line.split(None, 1)[0]) == userID) :
                    print("User found.")
                    succ = 1
                    newPass = input("New password: ")
                    this = userID + " " + newPass + " " + "0" + " " + "\n"
                    file2.write(this)
                else :
                    file2.write(line)
                line = file1.readline()
    os.remove("info.txt")
    os.rename("newinfo.txt" , "info.txt")
    if(succ == 1) :
        print("Password successfully changed.")