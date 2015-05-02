# This file only has to be ran once. If the database and tables are created, this can be omitted
# NapCorps Inc., User - dsantos date - 04/29/2015

from db.db_connect import connect_db
from mysql.connector import errors
from db.db_connect import mysql_check


def create_database(connection):

    # CREATE DATABASE
    try:
        cur = connection.cursor()

        query = '''
        CREATE DATABASE inventory DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci
        '''
        cur.execute(query)
        connection.close()

        print("Database created successfully!")

    except errors.DatabaseError as e:
        print(str(e))
        exit(1)


def create_table(connection):

    # CREATE TABLE
    try:
        cur = connection.cursor()

        # USE inventory database
        cur.execute('USE `inventory`')

        query = '''
        CREATE TABLE `items`(`id` INTEGER AUTO_INCREMENT UNIQUE NOT NULL,
                             `name` VARCHAR(255) NOT NULL,
                             `brand` VARCHAR(255),
                             `model` VARCHAR(255),
                             `description` TEXT,
                             `quantity` INTEGER NOT NULL,
                             `unit_cost` VARCHAR(8) NOT NULL,
                             `selling_price` VARCHAR(8),
                             `picture` BLOB,
                             PRIMARY KEY (`id`)) AUTO_INCREMENT=1;
        '''

        cur.execute(query)
        connection.close()

    except errors.ProgrammingError as e:
        print(str(e))

    print("Table created successfully!")

mysql_check()   # Check if it's possible to connect to MySQL
connect_db()    # Connect to  My SQL
create_database(connect_db())   # Create database
create_table(connect_db())  # Create needed for the program