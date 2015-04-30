from mysql.connector import connect
from mysql.connector import errors


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