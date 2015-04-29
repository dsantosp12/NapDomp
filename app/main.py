from app.create_item import create_item
from app.show_items import show_items

def show_menu():
    print("[C]REATE ITEM")
    print("[U]PDATE ITEM")
    print("[I]SSUE ITEM")
    print("[S]how ITEMS")
    print("[H]ELP")
    print("[Q]UIT")
    print("ENTER C, U, I, S, Q, OR H FOR HELP")


while True:
    show_menu()
    option = input("-> ").upper()

    if option == 'C':
        create_item()
        continue

    elif option == 'U':
        pass

    elif option == 'I':
        pass

    elif option == 'S':
        show_items()
        continue

    elif option == 'H':
        show_menu()
        continue

    elif option == 'Q':
        print("Exiting")
        break

    else:
        print("YOU MUST PROVIDE A VALID INPUT.\n")
        continue