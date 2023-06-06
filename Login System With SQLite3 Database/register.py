import sqlite3
def main() :
    database = sqlite3.connect('userlist.db')
    check = database.cursor()

    check.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='USERLIST'")
    if check.fetchone()[0] != 1 :
        check.execute('''CREATE TABLE USERLIST (USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL,BALANCE FLOAT NOT NULL);''')

    correct_input_check = 0
    username = input("Username: ")
    while correct_input_check != 3 :
        correct_input_check = 0
        check.execute("SELECT count(USERNAME) FROM USERLIST WHERE USERNAME=?",(username,))
        if check.fetchone()[0] > 0 :
            print("Username already taken.")
            username = input("Username: ")
        else :
            correct_input_check += 1
        if len(username) > 10 or len(username) < 4 :
            print("Username too long or too short.")
            username = input("Username: ")
        else :
            correct_input_check += 1
        if " " in username :
            print("Username contains space.")
            username = input("Username: ")
        else :
            correct_input_check += 1
        
    correct_input_check = 0
    password = input("Password: ")
    while correct_input_check != 2 :
        correct_input_check = 0
        if len(password) > 16 or len(password) < 4 :
            print("Password too long or too short.")
            password = input("Password: ")
        else :
            correct_input_check += 1
        if " " in password :
            print("Password contains space.")
            password = input("Password: ")
        else :
            correct_input_check += 1

    username = str(username)
    password = str(password)

    check.execute("INSERT INTO USERLIST (USERNAME,PASSWORD,BALANCE) VALUES (?,?,0)",(username, password,))
    database.commit()
    print("User",username,"created successfully.")

    database.close()