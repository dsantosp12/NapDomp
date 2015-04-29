from db.db_connect import connect_db
from app.inventory_classes import UpdateItem


def get_item_id():
    while True:
        print("1)Search by ID")
        print("2)Seach by NAME")
        print("[Q]uit - [B]ack")
        option = str(input("-> ")).upper()

        if option == '1':
            return search_by_id()
        elif option == '2':
            return search_by_name()
        elif option == 'Q':
            exit(1)
        elif option == 'B':
            return -1
        else:
            print("Please enter a valid input.")
            continue


def show_item(items):
    for item in items:
        print("ID: {}".format(item[0]))
        print("Name: {}".format(item[1]))
        print("Brand: {}".format(item[3]))
        print("Model: {}\n".format(item[4]))


def search_by_id():
    print("Please enter the ID")
    id_num = str(input("-> "))

    connection = connect_db()

    cur = connection.cursor()

    cur.execute('USE `inventory`')

    query = '''
               SELECT * FROM `items` WHERE `id` = {}
            '''.format(id_num)

    cur.execute(query)

    items = cur.fetchall()

    if not items:
        print("Item with ID : {} do not exist.\n".format(id_num))
        connection.close()
        return 0
    else:
        show_item(items)

    connection.close()

    return id_num


def search_by_name():
    print("Please enter the NAME")
    name = str(input("-> "))

    connection = connect_db()

    cur = connection.cursor()

    cur.execute('USE `inventory`')

    query = "SELECT * FROM `items` WHERE `name` = '%s'"

    cur.execute(query % name)

    items = cur.fetchall()

    if not items:
        print("Item with ID : {} do not exist.\n".format(name))
    else:
        show_item(items)

    connection.close()
    for item in items:
        item_id = item[0]

    return item_id


def update_item():

    while True:
        found_id = get_item_id()

        if found_id == -1:
            return

        print("Is this the right item?")
        print("(Y/n)")
        option = input("-> ").upper()

        if option == 'Y':
            break
        elif option == 'N':
            continue
        else:
            print("Please enter Y for yes or N for no.\n")
            continue

    item_name = str(input("Enter name: "))
    item_brand = str(input("Enter brand: "))
    item_model = str(input("Enter model: "))
    item_description = str(input("Enter a description: "))
    item_quantity = str(input("Enter quantity: "))
    item_unit_cost = str(input("Enter unit cost: "))
    item_selling_price = str(input("Enter selling price: "))
    # TODO: PIC will be selectable with the GUI later on.
    item_picture = str(input("Enter picture path: "))


    connection = connect_db()
    cur = connection.cursor()

    cur.execute('USE `inventory`')

    query = '''
        UPDATE `items` SET `name`=%s, `brand`=%s, `model`=%s,
               `description`=%s, `quantity`=%s, `unit_cost`=%s,
               `selling_price`=%s, `picture`=%s WHERE id = %s
    '''

    cur.execute(query, (item_name, item_brand, item_model,
                        item_description, item_quantity, item_unit_cost,
                        item_selling_price, item_picture, found_id))

    connection.commit()
    connection.close()
    print("Change made successfully!\n")