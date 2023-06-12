import pyodbc
DATABASELOCATION = r'C:\Users\Arjan\Downloads\Python2Access.accdb'
CONNECTION = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DATABASELOCATION+';'

def showData(query):
    
        conn = pyodbc.connect(CONNECTION)
        cursor = conn.cursor()
        cursor.execute(query) 
        for row in cursor.fetchall():
            print (row)
    
        cursor.close
        conn.close

showData('Select * from Address')