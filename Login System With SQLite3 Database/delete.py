import sqlite3

def main() :
    database = sqlite3.connect('userlist.db')
    check = database.cursor()

    check.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='USERLIST'")
    if check.fetchone()[0] != 1 :
        check.execute('''CREATE TABLE USERLIST (USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL,BALANCE FLOAT NOT NULL);''')

    username = input("Username: ")
    check.execute("SELECT count(USERNAME) from USERLIST Where USERNAME=?",(username,))
    if check.fetchone()[0] != 1 :
        print("User not found.")
    else :
        print("User",username,"found.")
        check.execute("SELECT PASSWORD from USERLIST WHERE USERNAME=?",(username,))
        real_password = check.fetchone()[0]
        print("Please enter password of user",username,"to delete this account:",end=" ")
        password = input()
        if password == real_password :
            choice = input("Please confirm to delete this account (Y|N): ").lower()
            if choice == "y" :
                check.execute("SELECT BALANCE from USERLIST WHERE USERNAME=?",(username,))
                if int(check.fetchone()[0]) >= 1 :
                    print("Can not delete user due to balance.")
                else :
                    check.execute("DELETE from USERLIST WHERE USERNAME=?",(username,))
                    database.commit()
                    print("User",username,"successfully deleted.")
            else :
                print("Process terminated.")