import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        con = sqlite3.connect('mydb.db')
        print("Connection is established: Database is created in memory")
        cursorObj = con.cursor()
    except Error:
        print(Error)

    finally:
        con.close()

sql_connection()

def sql_crdata():
    try:
        con = sqlite3.connect('mydb.db')
        print("connection is established to DATABASE ")
        con.execute("CREATE TABLE students(srno integer PRIMARY KEY, name text, contact_no text, address text)")
        con.commit()
    except Error:
        print(Error)
    finally:
        con.close()

#sql_crdata()

def sql_dataIN():
    try:
        con = sqlite3.connect('mydb.db')
        print("Program is inserting the data to DB")
        con.execute("INSERT INTO students VALUES(2,'Mak','8008503909','zone2')")
        con.commit()
        print("Completed succesfully")
    except Error:
        print(Error)
    finally:
        con.close()



sql_dataIN()

