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
                  '--------------------------------------')
            print("{:<11}{:<16}{:<25}{:<40}{:<15}{:<15}{:<10}".format("Name", "Brand", "Model", "Description",
                                                                      "Quantity", "Unit Cost", "Selling Price"))
            print('---------------------------------------------------------------------------------------------------'
                  '--------------------------------------')
            for item in items:
                print("{:<11}{:<18}{:<8}{:<58}{:<14}{:<17}{}".format(str(item[1]), str(item[3]), str(item[4]),
                                                               str(item[5]), str(item[2]), str(item[6]), str(item[7])))
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


def show_item(items):
    for item in items:
        print("ID: {}".format(item[0]))
        print("Name: {}".format(item[1]))
        print("Brand: {}".format(item[3]))
        print("Model: {}\n".format(item[4]))
