import pyodbc
DATABSELOCATION = r'C:\Users\kmb\OneDrive - Da Vinci College\Boeken\Python\Van stroomdiagrammen naar Python code\H22\Python2Access.accdb'
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DATABSELOCATION+';')
cursor = conn.cursor()

tabel = input("Welke tabel wil je zien : ")
sql = "select * from " + tabel
print(sql)
cursor.execute(sql)
   
for row in cursor.fetchall():
    print (row)