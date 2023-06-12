import pyodbc
DATABSELOCATION = r'C:\Python2Access.accdb'
CONNECT = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DATABSELOCATION+';'

def showData(query):
    try:
        conn = pyodbc.connect(CONNECT)
        cursor = conn.cursor()
        cursor.execute(query) 
        for row in cursor.fetchall():
            print (row)
    except:
        print ("Error")
    finally:
        cursor.close
        conn.close

user = input("Welke gebruiker wil je zien :")
sql = 'Select * from Person where idPerson = ' + user
showData( sql )