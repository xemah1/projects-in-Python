import sqlite3

def main() :
    database = sqlite3.connect('market.db')
    c = database.cursor()
    print("Categories are: fruit_vegetable|meat|breakfast|drink")
    category = input("Category: ")

    if category[0] == "f" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT FROM FRUIT_VEGETABLE WHERE AMOUNT > 0")
        for i in c.fetchall() :
            print(i[0]," x",i[1],end=" | ",sep="")
        print()
        print("add|delete|end")
        choice = input().lower()
        if choice[0] == "a" :

            print()
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM FRUIT_VEGETABLE WHERE NAME=?",(name,))
            if c.fetchone()[0] == 0 :
                amount = input("Amount of the Product: ")
                price = input("Price of the Product: ")
                c.execute("INSERT INTO FRUIT_VEGETABLE (NAME,AMOUNT,PRICE) VALUES (?,?,?)",(name,amount,price))
                database.commit()
            else :
                print("Product Already Exists.")
        elif choice[0] == "d" :
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM FRUIT_VEGETABLE WHERE NAME=?",(name,))
            if c.fetchone()[0] != 0 :
                c.execute("DELETE from FRUIT_VEGETABLE WHERE NAME=?",(name,))
            else :
                print("No match found.")

    elif category[0] == "m" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT FROM MEAT WHERE AMOUNT > 0")
        for i in c.fetchall() :
            print(i[0]," x",i[1],end=" | ",sep="")
        print()
        print("add|delete|end")
        choice = input().lower()
        if choice[0] == "a" :

            print()
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM MEAT WHERE NAME=?",(name,))
            if c.fetchone()[0] == 0 :
                amount = input("Amount of the Product: ")
                price = input("Price of the Product: ")
                c.execute("INSERT INTO MEAT (NAME,AMOUNT,PRICE) VALUES (?,?,?)",(name,amount,price))
                database.commit()
            else :
                print("Product Already Exists.")
        elif choice[0] == "d" :
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM MEAT WHERE NAME=?",(name,))
            if c.fetchone()[0] != 0 :
                c.execute("DELETE from MEAT WHERE NAME=?",(name,))
            else :
                print("No match found.")

    elif category[0] == "b" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT FROM BREAKFAST WHERE AMOUNT > 0")
        for i in c.fetchall() :
            print(i[0]," x",i[1],end=" | ",sep="")
        print()
        print("add|delete|end")
        choice = input().lower()
        if choice[0] == "a" :

            print()
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM BREAKFAST WHERE NAME=?",(name,))
            if c.fetchone()[0] == 0 :
                amount = input("Amount of the Product: ")
                price = input("Price of the Product: ")
                c.execute("INSERT INTO BREAKFAST (NAME,AMOUNT,PRICE) VALUES (?,?,?)",(name,amount,price))
                database.commit()
            else :
                print("Product Already Exists.")
        elif choice[0] == "d" :
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM BREAKFAST WHERE NAME=?",(name,))
            if c.fetchone()[0] != 0 :
                c.execute("DELETE from BREAKFAST WHERE NAME=?",(name,))
            else :
                print("No match found.")

    elif category[0] == "d" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT FROM DRINK WHERE AMOUNT > 0")
        for i in c.fetchall() :
            print(i[0]," x",i[1],end=" | ",sep="")
        print()
        print("add|delete|end")
        choice = input().lower()
        if choice[0] == "a" :

            print()
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM DRINK WHERE NAME=?",(name,))
            if c.fetchone()[0] == 0 :
                amount = input("Amount of the Product: ")
                price = input("Price of the Product: ")
                c.execute("INSERT INTO DRINK (NAME,AMOUNT,PRICE) VALUES (?,?,?)",(name,amount,price))
                database.commit()
            else :
                print("Product Already Exists.")
        elif choice[0] == "d" :
            name = input("Name of the Product: ").lower()
            c.execute("SELECT count(NAME) FROM DRINK WHERE NAME=?",(name,))
            if c.fetchone()[0] != 0 :
                c.execute("DELETE from DRINK WHERE NAME=?",(name,))
            else :
                print("No match found.")

    database.commit()
    database.close()

def control() :
    categories = []
    database = sqlite3.connect('market.db')
    c = database.cursor()

    c.execute("SELECT count(NAME) FROM FRUIT_VEGETABLE WHERE AMOUNT>0")
    if c.fetchone()[0] > 0 :
        categories.append("fruit_vegetable")

    c.execute("SELECT count(NAME) FROM MEAT WHERE AMOUNT>0")
    if c.fetchone()[0] > 0 :
        categories.append("meat")

    c.execute("SELECT count(NAME) FROM BREAKFAST WHERE AMOUNT>0")
    if c.fetchone()[0] > 0 :
        categories.append("breakfast")

    c.execute("SELECT count(NAME) FROM DRINK WHERE AMOUNT>0")
    if c.fetchone()[0] > 0 :
        categories.append("drink")

    database.close()
    return categories

def create() :

    database = sqlite3.connect('market.db')
    c = database.cursor()
    
    c.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='FRUIT_VEGETABLE'")
    if c.fetchone()[0] != 1 :
        c.execute('''CREATE TABLE FRUIT_VEGETABLE (NAME TEXT NOT NULL, AMOUNT INT NOT NULL, PRICE FLOAT NOT NULL);''')
    
    c.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='MEAT'")
    if c.fetchone()[0] != 1 :
        c.execute('''CREATE TABLE MEAT (NAME TEXT NOT NULL, AMOUNT INT NOT NULL, PRICE FLOAT NOT NULL);''')
    
    c.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='BREAKFAST'")
    if c.fetchone()[0] != 1 :
        c.execute('''CREATE TABLE BREAKFAST (NAME TEXT NOT NULL, AMOUNT INT NOT NULL, PRICE FLOAT NOT NULL);''')
    
    c.execute("SELECT count(name) from sqlite_master WHERE type='table' and name='DRINK'")
    if c.fetchone()[0] != 1 :
        c.execute('''CREATE TABLE DRINK (NAME TEXT NOT NULL, AMOUNT INT NOT NULL, PRICE FLOAT NOT NULL);''')

    database.close()

def customer(basket) :
    database = sqlite3.connect('market.db')
    c = database.cursor()
    choice = input("Category: ").lower()
    print("Input \"end\" will end process.")
    if choice[0] == "f" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT,PRICE FROM FRUIT_VEGETABLE WHERE AMOUNT > 0")
        seperator = 0
        for i in c.fetchall() :
            seperator += 1
            print(i[0]," x",i[1]," $",i[2],end=" | ",sep="")
            if seperator == 5 :
                print()
                print("| ",end="")
                seperator = 0
        print()
        print("Please type in the product and the amount you want to buy. \"Example: apple 25\"")
        choice = input().lower()
        try :
            if int(choice.split(None, 1)[1]) == int(choice.split(None, 1)[1]) :
                pass
        except IndexError :
            choice += " 1"
        c.execute("SELECT count(NAME),AMOUNT,PRICE FROM FRUIT_VEGETABLE WHERE NAME=?",(choice.split(None, 1)[0],))
        product = c.fetchall()
        if list(product[0])[0] == 1 :
            if list(product[0])[1] >= int(choice.split(None, 1)[1]) :
                c.execute("UPDATE FRUIT_VEGETABLE set AMOUNT=? WHERE NAME=?",(list(product[0])[1] - int(choice.split(None, 1)[1]), choice.split(None, 1)[0]))
                basket += list(product[0])[2] * int(choice.split(None, 1)[1])
            else :
                print("Product Amount not Enough.")
        else :
            print("Product not Found.")

    if choice[0] == "m" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT,PRICE FROM MEAT WHERE AMOUNT > 0")
        seperator = 0
        for i in c.fetchall() :
            seperator += 1
            print(i[0]," x",i[1]," $",i[2],end=" | ",sep="")
            if seperator == 5 :
                print()
                print("| ",end="")
                seperator = 0
        print()
        print("Please type in the product and the amount you want to buy. \"Example: chicken 25\"")
        choice = input().lower()
        try :
            if int(choice.split(None, 1)[1]) == int(choice.split(None, 1)[1]) :
                pass
        except IndexError :
            choice += " 1"
        c.execute("SELECT count(NAME),AMOUNT,PRICE FROM MEAT WHERE NAME=?",(choice.split(None, 1)[0],))
        product = c.fetchall()
        if list(product[0])[0] == 1 :
            if list(product[0])[1] >= int(choice.split(None, 1)[1]) :
                c.execute("UPDATE MEAT set AMOUNT=? WHERE NAME=?",(list(product[0])[1] - int(choice.split(None, 1)[1]), choice.split(None, 1)[0]))
                basket += list(product[0])[2] * int(choice.split(None, 1)[1])
            else :
                print("Product Amount not Enough.")
        else :
            print("Product not Found.")

    if choice[0] == "b" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT,PRICE FROM BREAKFAST WHERE AMOUNT > 0")
        seperator = 0
        for i in c.fetchall() :
            seperator += 1
            print(i[0]," x",i[1]," $",i[2],end=" | ",sep="")
            if seperator == 5 :
                print()
                print("| ",end="")
                seperator = 0
        print()
        print("Please type in the product and the amount you want to buy. \"Example: egg 25\"")
        choice = input().lower()
        try :
            if int(choice.split(None, 1)[1]) == int(choice.split(None, 1)[1]) :
                pass
        except IndexError :
            choice += " 1"
        c.execute("SELECT count(NAME),AMOUNT,PRICE FROM BREAKFAST WHERE NAME=?",(choice.split(None, 1)[0],))
        product = c.fetchall()
        if list(product[0])[0] == 1 :
            if list(product[0])[1] >= int(choice.split(None, 1)[1]) :
                c.execute("UPDATE BREAKFAST set AMOUNT=? WHERE NAME=?",(list(product[0])[1] - int(choice.split(None, 1)[1]), choice.split(None, 1)[0]))
                basket += list(product[0])[2] * int(choice.split(None, 1)[1])
            else :
                print("Product Amount not Enough.")
        else :
            print("Product not Found.")

    if choice[0] == "d" :
        print("Existing Products in this Category: |",end=" ")
        c.execute("SELECT NAME,AMOUNT,PRICE FROM DRINK WHERE AMOUNT > 0")
        seperator = 0
        for i in c.fetchall() :
            seperator += 1
            print(i[0]," x",i[1]," $",i[2],end=" | ",sep="")
            if seperator == 5 :
                print()
                print("| ",end="")
                seperator = 0
        print()
        print("Please type in the product and the amount you want to buy. \"Example: water 25\"")
        choice = input().lower()
        try :
            if int(choice.split(None, 1)[1]) == int(choice.split(None, 1)[1]) :
                pass
        except IndexError :
            choice += " 1"
        c.execute("SELECT count(NAME),AMOUNT,PRICE FROM DRINK WHERE NAME=?",(choice.split(None, 1)[0],))
        product = c.fetchall()
        if list(product[0])[0] == 1 :
            if list(product[0])[1] >= int(choice.split(None, 1)[1]) :
                c.execute("UPDATE DRINK set AMOUNT=? WHERE NAME=?",(list(product[0])[1] - int(choice.split(None, 1)[1]), choice.split(None, 1)[0]))
                basket += list(product[0])[2] * int(choice.split(None, 1)[1])
            else :
                print("Product Amount not Enough.")
        else :
            print("Product not Found.")

    database.commit()
    database.close()
    return basket