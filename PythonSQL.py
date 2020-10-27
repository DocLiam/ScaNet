def join_multiple(arrayList, delimList, skipLast):
    """Joins multiple arrays with specific relevant delimeters"""
    stringReturn = ""
    listLen = len(arrayList[0])
    cutLength = 0

    for i in range(listLen):
        for j in range(len(arrayList)):
            stringReturn += arrayList[j][i] + delimList[j]

    if skipLast:
        cutLength = len(stringReturn.split(delimList[-1])[-2])

    return stringReturn[:-2-cutLength]

def where_table(fieldArray1, fieldArray2, comparatorArray, operatorArray, skipLast):
    """Returns a query selection statement using two compared fields and the operator for comparison"""
    queryComponent = "WHERE " + join_multiple([fieldArray1, comparatorArray, fieldArray2, operatorArray], [" ", " ", " ", " "], skipLast)

    return queryComponent

def update_table(tblName, attributeArray, valuesArray, skipLast):
    """Returns a query component that will update the values of attributes in a table"""
    queryComponent = "UPDATE " + tblName + "\nSET " + join_multiple([attributeArray, valuesArray], [" = ", ", "], skipLast)

    return queryComponent

def order_table(attributeArray, orderArray, skipLast):
    """Returns query component that will sort by attributes according to a specified order"""
    queryComponent = "ORDER BY " + join_multiple([attributeArray, orderArray], [" ", ", "], skipLast)

    return queryComponent

def create_table(tblName, attributeArray, typeArray, skipLast):
    """Returns a query component that will create a table with attributes and given types"""
    queryComponent = "CREATE TABLE " + tblName + " (\n" + join_multiple([attributeArray, typeArray], [" ", ",\n"], skipLast) + "\n)"

    return queryComponent

def alter_table(tblName, attributeName, typeName, skipLast):
    """Returns a query that will add a new attribute to a table"""
    queryComponent = "ALTER TABLE " + tblName + "\nADD " + attributeName + " " + typeName

    return queryComponent

#TESTING
print(where_table(["ID", "Surname"], ['"123"', '"Smith"'], ["==", "=="], ["AND", "AND"], True))
print(update_table("DetailsTbl", ["ID", "Surname"], ['"123"', '"Smith"'], False))
print(order_table(["ID", "Surname"], ["DESC", "ASC"], False))
print(create_table("DetailsTbl", ["ID", "Surname"], ["int", "varchar(32)"], False))
print(alter_table("DetailsTbl", "Firstname", "varchar(32)", False))

def search_table(tblName, valuesArray = ["*"], filterArray = [""], orderArray = ["Asc"]):
    for i in range(len(valuesArray) - len(filterArray)):
        filterArray.append("")
    string = "Select "+",".join(valuesArray)+" from "+tblName
    string += " where "+", ".join([valuesArray[i] + " = " + filterArray[i] for i in range(len(valuesArray))]) #Upon creation, join_multiple() did not exist. Line is a single line alternative.
    string += " Order By " + ",".join(orderArray)
    print(string)
