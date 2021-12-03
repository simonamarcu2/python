import sqlite3


def register():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    while True:
            login = input("\nEnter your login: ")
            for i in all_results:
                if login == i[0]:
                    print("This login alredy used!")
                    register()
            password = input("Enter password: ")
            new_user = (login, password)
            password_check = input("Enter password secondary: ")
            if password == password_check:
                cur.execute("INSERT INTO users VALUES(?, ?);", new_user)
                conn.commit()
                print("\nYour registered new account")
                menu()
            elif password != password_check:
                print("\nPasswords not the same, please enter again")


def menu_user():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    while True:
        print("""\n1)Check all accounts
2)Delete account
3)Logout""")
        user_choise = int(input("You choose: "))
        if user_choise == 1:
            cur.execute("SELECT * FROM users;")
            all_results = cur.fetchall()
            print("----------------")
            for i in all_results:
                print(i)
            print("______________")
        elif user_choise == 2:
            deleted_acc = input("Enter login of account, that you need to delete: ")
            for i in all_results:
                if deleted_acc in i:
                    sql_update_query = """DELETE from users where login = ?"""
                    cur.execute(sql_update_query, (deleted_acc, ))
                    conn.commit()
                    print(f"Account {deleted_acc} deleted from DB")
                    menu_user()
            print(f"Account {deleted_acc} not find on DB")
        elif user_choise == 3:
            menu()


def menu():
    conn = sqlite3.connect('orders.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    pass TEXT);
    """)
    conn.commit()
    print("""\n1)Log in to the account
2)Register new account
3)Exit""")
    user_choice = int(input("You choose: "))
    if user_choice == 2:
        register()
    elif user_choice == 1:
        while True:
            login = input("\nEnter your login: ")
            password = input("Enter password: ")
            user = (login, password)
            cur.execute("SELECT * FROM users;")
            all_results = cur.fetchall()
            if user in all_results:
                print("""------------  
You entered :)
-------------""")
                menu_user()
            else:
                print("Login or password not true")

    elif user_choice == 3:
        print("\nBye!!")
        quit()


menu()
