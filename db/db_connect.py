from mysql.connector import connect
from mysql.connector import errors

from subprocess import call


def mysql_check():
    try:
        if call(["/usr/local/Cellar/mysql/5.6.24/bin/mysql.server", "status"]) == 3:
            if call(["/usr/local/Cellar/mysql/5.6.24/bin/mysql.server", "start"]) != 0:
                print("Mysql.server couldn't be opened...")
                print("Exiting..")
                exit(9)
            print("MySQL Status: Running...")
    except FileNotFoundError as e:
        print(e)
        exit(9)


def connect_db():

    try:
        connection = connect(host='localhost',
                             user='root',
                             password='',
                             charset='utf8mb4')

    except (errors.DatabaseError, errors.InterfaceError) as error:
        print(str(error))
        exit()

    return connection