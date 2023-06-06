import sqlite3
def main() :
    database = sqlite3.connect('userlist.db')
    check = database.cursor()

    check.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='USERLIST'")
    if check.fetchone()[0] != 1 :
        check.execute('''CREATE TABLE USERLIST (USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL,BALANCE FLOAT NOT NULL);''')

    name_list = list(check.execute("SELECT USERNAME, PASSWORD, BALANCE FROM USERLIST"))
    print('-'*75)
    for line in name_list :
        print("Username:",line[0],' '*(10-len(line[0])),"Password:",line[1],' '*(16-len(line[1])),"Balance:",line[2])

    print('-'*75)
    print("User list successfully listed.")

    database.close()