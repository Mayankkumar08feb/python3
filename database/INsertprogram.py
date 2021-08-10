import sqlite3
from sqlite3 import Error
con = sqlite3.connect('mydb.db')
con.execute("INSERT INTO students VALUES(1,'Mayank','8008503635','zone1')")
con.commit()
con.close()


'''
def sql_dataIN():
    try:
        con = sqlite3.connect('mydb.db')
        print("Program is inserting the data to DB")
        con.execute("INSERT INTO students(1,'Mayank','8008503635','zone1')")
        con.commit()
        print("Completed succesfully")
    except Error:
        print(Error)
    finally:
        con.close()

sql_dataIN()
'''

