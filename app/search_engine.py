from db.db_connect import connect_db
# TODO: Create only one show item.
from app.update_item import show_item


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