import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\progr\Documents\sandbox\Python\test.accdb;')
cursor = conn.cursor()
cursor.execute("""
                SELECT * FROM Table1
                where * = '1'
                """)

def order_by(tblName, paramArray):
    

def create_table(tblName, )

def search_table(tblName, valuesArray, filterArray = [], order_by = "Asc"):
    string = "Select "
    print(cursor.execute(string))
