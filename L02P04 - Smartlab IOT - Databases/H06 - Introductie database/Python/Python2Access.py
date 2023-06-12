import pyodbc
# Some other example server values are
#SERVER = 'localhost\sqlexpress' # for a named instance
#SERVER = 'myserver,port' # to specify an alternate port
#SERVER   = 'tcp:myserver.database.windows.net' 
DATABASE = r'C:\Users\kmb\Downloads\LPEMO19K4F1.accdb'
#USERNAME = 'myusername' 
#PASSWORD = 'mypassword' 

#CONNECTION     = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USERNAME+';PWD='+ PASSWORD
CONNECTION      = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DATABASE+';'
    
def showData(query):
    try:
        conn = pyodbc.connect(CONNECTION)
        cursor = conn.cursor()
        cursor.execute(query) 
        for row in cursor.fetchall():
            print (row)
    except:
        print("Error")
    finally:   
        cursor.close
        conn.close

user = input("Welke gebruiker : ")
showData('Select * from Person where idPerson = ' + user)
