import sqlite3
import gatesoav2sub5

def main() :
    database = sqlite3.connect('userlist.db')
    check = database.cursor()
    
    check.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='USERLIST'")
    if check.fetchone()[0] != 1 :
        check.execute('''CREATE TABLE USERLIST (USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL,BALANCE FLOAT NOT NULL);''')
    
    username = input("Username: ")
    password = input("Password: ")
    check.execute("SELECT count(USERNAME) FROM USERLIST WHERE USERNAME=?",(username,))
    if check.fetchone()[0] == 1 :
        check.execute("SELECT PASSWORD FROM USERLIST WHERE USERNAME=?",(username,))
        if check.fetchone()[0] == password :
            print("Login successful.")
        else :
            username = "a"
            print("Wrong username or password.")
    else :
        print("Wrong username or password.")
        username = "a"
    if username != "a" :
        end = True
        while end :
            print("information|deposit|withdraw|transfer|gates of ankara|logout")
            choice = input().lower()
            if choice[0] == "i" :
                name_list = list(check.execute("SELECT USERNAME, PASSWORD, BALANCE FROM USERLIST WHERE USERNAME=?",(username,)))
                print('-'*75)
                for line in name_list :
                    print("Username:",line[0],' '*(10-len(line[0])),"Password:",line[1],' '*(16-len(line[1])),"Balance:",f"{line[2]:.2f}")
                print('-'*75)
            elif choice[0] == "d" :
                try :
                    deposit = float(input("Deposit Amount: "))
                except ValueError :
                    print("Wrong Input.")
                    deposit = 0
                if deposit < 0 :
                    deposit = 0
                print("Depositing",deposit,"USD")
                print('-'*20)
                check.execute("SELECT BALANCE FROM USERLIST WHERE USERNAME=?",(username,))
                balance = check.fetchone()[0]
                balance = f"{balance + deposit:.2f}"
                check.execute("UPDATE USERLIST set BALANCE=? WHERE USERNAME=?",(balance, username,))
                database.commit()

            elif choice[0] == "w" :
                try :
                    withdraw = float(input("Withdraw Amount: "))
                except ValueError :
                    print("Wrong Input.")
                    withdraw = 0
                check.execute("SELECT BALANCE FROM USERLIST WHERE USERNAME=?",(username,))
                balance = check.fetchone()[0]
                if withdraw < 0 or int(balance) < withdraw :
                    withdraw = 0
                    print("Insufficient Balance.")
                else :
                    print("Withdrawing",withdraw,"USD")
                print('-'*20)
                balance = f"{balance - withdraw:.2f}"
                check.execute("UPDATE USERLIST set BALANCE=? WHERE USERNAME=?",(balance, username,))
                database.commit()
            elif choice[0] == "t" :
                desired_username = input("Username to Transfer: ")
                check.execute("SELECT count(USERNAME) FROM USERLIST WHERE USERNAME=?",(desired_username,))
                if check.fetchone()[0] != 1 :
                    print("User not found.")
                else :
                    try :
                        send = float(input("Amount to Send: "))
                    except ValueError :
                        print("Wrong Input.")
                    check.execute("SELECT BALANCE FROM USERLIST WHERE USERNAME=?",(username,))
                    balance = check.fetchone()[0]
                    if send > balance :
                        print("Insufficient Balance.")
                    else :
                        check.execute("UPDATE USERLIST set BALANCE=? WHERE USERNAME=?",(balance - send, username,))
                        check.execute("SELECT BALANCE FROM USERLIST WHERE USERNAME=?",(desired_username,))
                        balance = check.fetchone()[0]
                        check.execute("UPDATE USERLIST set BALANCE=? WHERE USERNAME=?",(send + balance, desired_username,))
                        print("Transaction Successful.")
                        database.commit()
            elif choice[0] == "g" :
                check.execute("SELECT BALANCE FROM USERLIST WHERE USERNAME=?",(username,))
                balance = check.fetchone()[0]
                result,bet = gatesoav2sub5.game(balance)
                result = float(result)
                bet = float(bet)
                result -= bet
                float("{0:.2f}".format(balance))
                float("{0:.2f}".format(result))
                check.execute("UPDATE USERLIST set BALANCE=? WHERE USERNAME=?",(balance + result,username,))
                database.commit()
            else :
                end = False
                print('-'*50)
                database.close()