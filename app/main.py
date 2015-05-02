from app.create_item import create_item
from app.update_item import update_item
from app.show_items import show_items
from app.issue_item import issue_item
from app.help import show_help
from db.db_connect import connect_db
from db.db_connect import mysql_check


def show_menu():
    print("[C]REATE ITEM")
    print("[U]PDATE ITEM")
    print("[I]SSUE ITEM")
    print("[S]HOW ITEMS")
    print("[H]ELP")
    print("[Q]UIT")
    print("ENTER C, U, I, S, Q, OR H FOR HELP")

# Check MySQL Status
mysql_check()

while True:
    connection = connect_db()

    show_menu()
    option = input("-> ").upper()

    if option == 'C':
        create_item()
        continue

    elif option == 'U':
        update_item()
        continue

    elif option == 'I':
        issue_item()
        pass

    elif option == 'S':
        show_items()
        continue

    elif option == 'H':
        show_help()
        continue

    elif option == 'Q':
        print("Exiting")
        break

    else:
        print("YOU MUST PROVIDE A VALID INPUT.\n")
        continue

connection.close()