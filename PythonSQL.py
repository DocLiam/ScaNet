def join_multiple(arrayList, delimList):
    """Joins multiple arrays with specific relevant delimeters"""
    stringReturn = ""
    listLen = len(arrayList[0])

    for i in range(listLen):
        for j in range(len(arrayList)):
            stringReturn += arrayList[j][i] + delimList[j]

        stringReturn += " "

    return stringReturn[:-2]

def where_table(fieldArray1, fieldArray2, comparatorArray, operatorArray):
    """Returns a query selection statement using two compared fields and the operator for comparison"""
    queryComponent = "WHERE " + join_multiple([fieldArray1, comparatorArray, fieldArray2, operatorArray], [" ", " ", " ", " "])

    return queryComponent

def update_table(tblName, attributeArray, valuesArray):
    """Returns a query component that will update the values of attributes in a table"""
    queryComponent = "UPDATE " + tblName + "\nSET " + join_multiple([attributeArray, valuesArray], [" = ", ", "])

    return queryComponent

def order_table(attributeArray, orderArray):
    """Returns query component that will sort by attributes according to a specified order"""
    queryComponent = "ORDER BY " + join_multiple([attributeArray, orderArray], [" ", ", "])

    return queryComponent

def create_table(tblName, attributeArray, typeArray):
    """Returns a query component that will create a table with attributes and given types"""
    queryComponent = "CREATE TABLE " + tblName + " (\n" + join_multiple([attributeArray, typeArray], [" ", "\n"]) + "\n)"

    return queryComponent

def alter_table(tblName, attributeName, typeName):
    """Returns a query that will add a new attribute to a table"""
    queryComponent = "ALTER TABLE " + tblName + "\nADD " + attributeName + " " + typeName

    return queryComponent

print(where_table())

def search_table(tblName, valuesArray = ["*"], filterArray = [""], orderArray = ["Asc"]):
    for i in range(len(valuesArray) - len(filterArray)):
        filterArray.append("")
    string = "Select "+",".join(valuesArray)+" from "+tblName
    string += " where "+", ".join([valuesArray[i] + " = " + filterArray[i] for i in range(len(valuesArray))]) #Upon creation, join_multiple() did not exist. Line is a single line alternative.
    string += " Order By " + ",".join(orderArray)
    print(string)
