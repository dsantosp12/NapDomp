from db.db_connect import connect_db
from app.search_engine import search_by_id, search_by_name
from app.show_items import show_items


def get_item():
    while True:
        print("1)Search by ID")
        print("2)Seach by NAME")
        print("3)Show inventory")
        print("[Q]uit - [B]ack")
        option = str(input("-> ")).upper()

        if option == '1':
            return search_by_id()
        elif option == '2':
            return search_by_name()
        elif option == '3':
            show_items()
            continue
        elif option == 'Q':
            exit(1)
        elif option == 'B':
            return -1
        else:
            print("Please enter a valid input.")
            continue


def issue_item():
    connection = connect_db()

    cur = connection.cursor()
    cur.execute('USE `inventory`')

    item_id = get_item()

    if item_id == -1:
        return

    query = "SELECT `quantity`, `name` FROM `items` WHERE `id` = '%s'"

    cur.execute(query % item_id)

    item_quantity = cur.fetchall()

    for item_fetched in item_quantity:
        item_quantity_available = item_fetched[0]
        name = item_fetched[1]

    print("How many {} you are selling?".format(str(name)))
    quantity_issued = int(input("->"))

    if item_quantity_available < quantity_issued:
        print("No enough {} in stock.".format(name))
        print("Avaliable right now: {}".format(item_quantity_available))
    else:
        updated_quantity = item_quantity_available - quantity_issued

        query ="UPDATE `items` SET  `quantity`=%s WHERE `id` = %s"

        try:
            cur.execute(query, (updated_quantity, item_id))
            connection.commit()
        except Exception as e:
            print(e)
        connection.close()
        print("Item issued successfully\n")