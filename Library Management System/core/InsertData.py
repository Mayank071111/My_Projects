# This Module has the Functions to Insert the Data in the MySQL Tables

# Importing Required Modules

import csv
import mysql.connector as con

# Functions


def InsertDatabooks():
    """
    InsertDatabooks() -> Inserts all the book details in the book _info Table

    Parameters -> None
    """

    mn = con.connect(host="localhost",
                     user="root",
                     password="abcdef",
                     database="library")

    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the absolute path of the file on your computer
    try:
        with open(FULL_PATH_TO_THE_CSV_FILE) as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                cur.execute(
                    'INSERT INTO book _info VALUES(%s,%s,%s,%s)', row) # %s is used for pssing arguments
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    finally:
        mn.commit()  # Important: Committing the Changes
        cur.close()
        mn.close()
