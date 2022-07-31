import os
import sys


def main(userID) :
    k = 0
    while k == 0 :
        print("-------------------------------------")
        print("Possible actions are listed below. Input Example: 2")
        print("1. See your account status.")
        print("2. Deposit money.")
        print("3. Withdraw money.")
        print("4. Transfer money.")
        print("5. Log out.")
        choice = input()
        if (choice == "1") :
            status(userID)
        if (choice == "2") :
            deposit(userID)
        if (choice == "3") :
            withdraw(userID)
        if (choice == "4") :
            transfer(userID)
        if (choice == "5") :
            print("Successfully logged out.")
            k += 1
    
def status(userID) :
    print("-------------------------------------")
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            if (line.split(None, 3)[0] == userID) :
                print()
                print("Username: " + line.split(None, 3)[0], end=" | ")
                print("Password: " + line.split(None, 3)[1], end=" | ")
                print("Balance: " + line.split(None, 3)[2])
                print()
                break
            line = f.readline()

def deposit(userID) :
    print("-------------------------------------")
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            if (line.split(None, 3)[0] == userID) :
                print()
                w = input("Deposit Amount: ")
                while (isinstance(w, int)) and (int(w) > int(0)) :
                    print("Wrong amount.")
                    w = input("Deposit Amount: ")
                a = int(line.split(None, 3)[2]) + int(w)
                lineR = line.split(None, 3)[0] + " " + line.split(None, 3)[1] + " " + str(a) + " " + "\n"
                break
            line = f.readline()
    succ = 0
    with open(os.path.join(sys.path[0], "newinfo.txt"), "w") as file2:
        with open(os.path.join(sys.path[0], "info.txt"), "r") as file1:
            line = file1.readline()
            while line :
                if((line.split(None, 1)[0]) == userID) :
                    succ = 1
                else :
                    file2.write(line)
                line = file1.readline()
            file2.write(lineR)
    os.remove("info.txt")
    os.rename("newinfo.txt" , "info.txt")
    if(succ == 1) :
        print("Deposit successful.")
        print()

def withdraw(userID) :
    print("-------------------------------------")
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            if (line.split(None, 3)[0] == userID) :
                w = input("Withdraw Amount: ")
                while (isinstance(w, int)) and (int(w) > int(line.split(None, 3)[2])) and (int(w) < 0):
                    print("Wrong amount.")
                    w = input("Withdraw Amount: ")
                a = int(line.split(None, 3)[2]) - int(w)
                lineR = line.split(None, 3)[0] + " " + line.split(None, 3)[1] + " " + str(a) + " " + "\n"
                break
            line = f.readline()
    succ = 0
    with open(os.path.join(sys.path[0], "newinfo.txt"), "w") as file2:
        with open(os.path.join(sys.path[0], "info.txt"), "r") as file1:
            line = file1.readline()
            while line :
                if((line.split(None, 1)[0]) == userID) :
                    succ = 1
                else :
                    file2.write(line)
                line = file1.readline()
            file2.write(lineR)
    os.remove("info.txt")
    os.rename("newinfo.txt" , "info.txt")
    if(succ == 1) :
        print("Withdrawal successful.")
        
def userFinder() :
    print("-------------------------------------")
    userIDchoice = input("Target username: ")
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            if (line.split(None, 3)[0] == userIDchoice) :
                break
            line = f.readline()
    if (len(line) > 1) :
        if (line.split(None, 3)[0] == userIDchoice) :
            print("User " + userIDchoice + " found.")
            return userIDchoice
    else :
        print("User could not be found.")
        return 0

def transfer(userID) :
    userIDchoice = userFinder()
    if (userIDchoice == 0) :
        return 0
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            if (line.split(None, 3)[0] == userID) :
                w = input("Transfer Amount: ")
                while (isinstance(w, int)) and (int(w) > int(line.split(None, 3)[2])) and (int(w) < 0):
                    print("Wrong amount.")
                    w = input("Transfer Amount: ")
                a = int(line.split(None, 3)[2]) - int(w)
                lineR = line.split(None, 3)[0] + " " + line.split(None, 3)[1] + " " + str(a) + " " + "\n"
                break
            line = f.readline()
    succ = 0
    with open(os.path.join(sys.path[0], "newinfo.txt"), "w") as file2:
        with open(os.path.join(sys.path[0], "info.txt"), "r") as file1:
            line = file1.readline()
            while line :
                if((line.split(None, 1)[0]) == userID) :
                    succ += 1
                else :
                    file2.write(line)
                line = file1.readline()
            file2.write(lineR)
    os.remove("info.txt")
    os.rename("newinfo.txt" , "info.txt")
    with open(os.path.join(sys.path[0], "info.txt"), "r") as f:
        line = f.readline()
        while line :
            if (line.split(None, 3)[0] == userIDchoice) :
                a = int(line.split(None, 3)[2]) + int(w)
                lineR = line.split(None, 3)[0] + " " + line.split(None, 3)[1] + " " + str(a) + " " + "\n"
                break
            line = f.readline()
    with open(os.path.join(sys.path[0], "newinfo.txt"), "w") as file2:
        with open(os.path.join(sys.path[0], "info.txt"), "r") as file1:
            line = file1.readline()
            while line :
                if((line.split(None, 1)[0]) == userIDchoice) :
                    succ += 1
                else :
                    file2.write(line)
                line = file1.readline()
            file2.write(lineR)
    os.remove("info.txt")
    os.rename("newinfo.txt" , "info.txt")
    if(succ == 2) :
        print("Transfer successful.")