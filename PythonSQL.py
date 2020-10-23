import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\progr\Documents\sandbox\Python\test.accdb;')
cursor = conn.cursor()

def join_multiple(arrayList, delimList):
    """Joins multiple arrays with specific relevant delimeters."""
    stringReturn = ""
    listLen = len(arrayList[0])

    for i in range(listLen):
        for j in range(len(arrayList)):
            stringReturn += arrayList[j][i] + delimList[j]

        stringReturn += " "

    return stringReturn[:-2]

def order_table(attributeArray, orderArray):
    """Returns query component that will sort by attributes according to a specified order"""
    queryComponent = "ORDER BY " + join_multiple([attributeArray, orderArray], [" ", ","])

    return queryComponent

def create_table(tblName, attributeArray, typeArray):
    """Returns a query component that will create a table with attributes and given types"""
    queryComponent = "CREATE TABLE " + tblName + " (\n" + join_multiple([attributeArray, typeArray], [" ", "\n"]) + "\n);"

    return queryComponent

def alter_table(tblName, attributeName, typeName):
    queryComponent = "ALTER TABLE " + tblName + "\nADD " + attributeName + " " + typeName + ";"

    return queryComponent

def search_table(tblName, valuesArray = ["*"], filterArray = [""], orderArray = ["Asc"]):
    for i in range(len(valuesArray) - len(filterArray)):
        filterArray.append("")
    string = "Select "+",".join(valuesArray)+" from "+tblName
    string += " where "+", ".join([valuesArray[i] + " = " + filterArray[i] for i in range(len(valuesArray))]) #Upon creation, join_multiple() did not exist. Line is a single line alternative.
    string += " Order By " + ",".join(orderArray)
    print(string)
