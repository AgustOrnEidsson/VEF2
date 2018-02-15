#Ágúst Örn Eiðsson
#13.2.18

import sqlite3,sys

def login():
    while True:
        username=input("Sláðu inn notandanafn: ")
        password=input("Sláðu inn lykilorð: ")

        with sqlite3.connect("gogn.db") as db:
            cursor=db.cursor()

        leit=("SELECT * FROM USERS WHERE username = ? AND password = ?")

        cursor.execute(leit,[(username),(password)])

        skil=cursor.fetchall()

        if skil:
            for x in skil:
                print("Velkominn",x[2])
            #return ("Exit")
            break

        else:
            print("Notandanafn eða lykilorð er ekki rétt")
            aftur=input("Viltu reyna aftur? (sláðu inn n ef þú vilt hætta)").lower()
            if aftur=="n":
                print("Bless Bless")
             #   return ("Exit")
                break

def new():
    found=0
    while found==0:
        username=input("Sláðu inn notandanafn: ")

        with sqlite3.connect("gogn.db") as db:
            cursor=db.cursor()

        leit=("SELECT * FROM USERS WHERE username = ?")
        cursor.execute(leit,[(username)])

        if cursor.fetchall():
            print("Notandanafn er nú þegar í notkun, reyndu aftur")

        else:
            found=1

    name1=input("Sláðu inn first name: ")
    name2=input("Sláðu inn last name: ")
    password1 = input("Sláðu inn lykilorð: ")
    password2 = input("Sláðu inn lykilorð: ")

    while password1!=password2:
        print("Lykilorðin eru ekki eins")
        password1 = input("Sláðu inn lykilorð: ")
        password2 = input("Sláðu inn lykilorð: ")

    setjaInn=('''
    INSERT INTO USERS(username,firstname,lastname,password)
    VALUES (?,?,?,?)''')

    cursor.execute(setjaInn, [(username),(name1),(name2),(password2)])

    db.commit()

def menu():
    while True:
        print("Velkominn :)")
        menu=('''
        1 - Nýskráning
        2 - Innskráning
        3 - Exit\n
        ''')

        svar=input(menu)


        if svar=="1":
            new()

        elif svar=="2":
            login()

        elif svar=="3":
            print("Bless bless")
            sys.exit()

        else:
            print("Rangur innsláttur")

menu()