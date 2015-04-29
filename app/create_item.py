from app.inventory_classes import CreateItem
from db.db_connect import connect_db


def create_item():

    item_name = str(input("Enter name: "))
    item_brand = str(input("Enter brand: "))
    item_model = str(input("Enter model: "))
    item_description = str(input("Enter a description: "))
    item_quantity = str(input("Enter quantity: "))
    item_unit_cost = str(input("Enter unit cost: "))
    item_selling_price = str(input("Enter selling price: "))
    # TODO: PIC will be selectable with the GUI later on.
    item_picture = str(input("Enter picture path: "))

     # Item object
    item = CreateItem(item_name, item_quantity,item_brand,
                      item_model, item_description, item_unit_cost,
                      item_selling_price, item_picture)

    try:
        # Connect to database
        connection = connect_db()
        cur = connection.cursor()

        # Select inventory db
        cur.execute('USE `inventory`')

        # Insertion
        # TODO: check how to prevent database injections
        query = '''
                INSERT INTO `items` (`name`, `brand`, `model`,
                                     `description`, `quantity`,`unit_cost`,
                                     `selling_price`, `picture`)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
                '''

        # Execute query, commit, and close
        cur.execute(query, (str(item.name), str(item.brand), str(item.model),
                            str(item.description), str(item.quantity), str(item.unit_cost),
                            str(item.selling_price), str(item.picture)))

        connection.commit()
        connection.close()

    except Exception as e:
        print(e)
        exit()

    # Success
    print('Item created successfully.\n')
