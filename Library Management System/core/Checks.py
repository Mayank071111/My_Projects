# This Module has the Functions that Verify the Requirements of the Project

# Importing Required Modules

import mysql.connector as con
from mysql.connector.errors import ProgrammingError, Error
import core.InsertData as Insert

# Functions


def CheckDatabase():
    """
    CheckDatabase() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = con.connect(host="localhost", user="root",
                     database="", password="abcdef")
    cur = db.cursor()
    result = None

    try:
        cur.execute("use library;")
    except ProgrammingError:
        print("Database does not Exist!")
        result = False
    else:
        result = True

    if result is True:
        print("Database exists!")
    else:
        print("Creating Database with the Required Tables..")
        print("Please be Patient!")
        cur.execute("create database library;")
        cur.execute("use library;")
        CreateTables()
        print("Database and Tables Created!")

    cur.close()
    db.close()


def CreateTables():
    """
    CreateTables() -> Creates all the Required Tables

    Parameters -> None
    """

    db = con.connect(host="localhost", user="root",
                     database="library", password="abcdef")
    cur = db.cursor()

    cur.execute(
        "create table book_info (book_No varchar(10) NOT NULL, Book_Name varchar(30) NOT NULL, book_issue_Time varchar(20) NOT NULL, book_Deposit_Time varchar(20) NOT NULL);")

    cur.execute("create table students (student_Name varchar(30) NOT NULL, Mobile_No varchar(10) NOT NULL,book_id int(5),class varchar(20) NOT NULL);")
# cur.execute("create table students (studentroll_No int NOT NULL, student_Name varchar(30) NOT NULL, Mobile_No varchar(10) NOT NULL,book_id int(5),class varchar(20) NOT NULL,Department varchar(20) NOT NULL);")

    Insert.InsertDatabooks()

    cur.close()
    db.close()


def CheckConnection():
    """
    CheckConnection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(host='localhost',
                                 database='',
                                 user="root",
                                 password="abcdef")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_Info)

    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True
