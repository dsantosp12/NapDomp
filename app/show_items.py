from db.db_connect import connect_db


def show_items():
    try:
        connection = connect_db()
        cur = connection.cursor()

        cur.execute("USE `inventory`")

        query = "SELECT * FROM `items`"

        cur.execute(query)

        items = cur.fetchall()
        if not items:
            print('You have 0 items in the database.')
        else:
            print('---------------------------------------------------------------------------------------------------'
                  '---------------------------')
            print("Name\t\tBrand\t\tModel\t\t\t\t\t\tDescription\t\t\t\t\t\t\t\t\tUnit Cost\t\tSelling Price")
            print('---------------------------------------------------------------------------------------------------'
                  '---------------------------')
            for item in items:
                print("{:<12}{:<14}{:<5}{:<67}{:<16}{}".format(str(item[1]), str(item[2]), str(item[3]),
                                                                    str(item[4]), str(item[5]), str(item[6])))
            print("\n")

            while True:
                print("[B]ack - [Q]uit")
                option = input("-> ").upper()
                if option == 'Q':
                    exit(1)
                elif option == 'B':
                    print("Going back to menu.\n")
                    break
                else:
                    print("Please enter Q or B")

                    continue

    except Exception as e:
        print(e)
        exit(2)