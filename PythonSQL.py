import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\progr\Documents\sandbox\Python\test.accdb;')
cursor = conn.cursor()
cursor.execute("""
                SELECT * FROM Table1
                where * = '1'
                """)

def join_multiple(arrayList):
    stringReturn = ""

def order_table(paramArray, orderArray):
    queryComponent = "ORDER BY " +


def create_table(tblName, )

def search_table(tblName, valuesArray = ["*"], filterArray = [""], orderArray = ["Asc"]):
    for i in range(len(valuesArray) - len(filterArray)):
        filterArray.append("")
    string = "Select "+",".join(valuesArray)+" from "+tblName
    string +=" where "+", ".join([valuesArray[i] + " = " + filterArray[i] for i in range(len(valuesArray))])
    string += "Order By " + ",".join(orderArray)
    print(string)
