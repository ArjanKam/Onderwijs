import pyodbc
DATABSELOCATION = r'C:\Users\kmb\OneDrive - Da Vinci College\Boeken\Python\Van stroomdiagrammen naar Python code\H25\RaspberryValues.accdb'
DRIVER = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
SQL = "EXEC [spInsertData] ?, ?"
TIME_INTERVAL = 60

previousData = dict()
def WriteData(counter, params):
    key = params[0]
    value_unchanged = key in previousData and previousData[key] == params[1]
    if value_unchanged and counter % TIME_INTERVAL != 0:
        return;
    previousData[key] = params[1]
    print(">> Writing data ", counter, params, previousData )
    conn = pyodbc.connect(DRIVER + DATABSELOCATION + ';', autocommit=True)
    cursor = conn.cursor()
    try:
        cursor.execute(SQL, params)
    finally:
        cursor.close
        conn.close
        
if __name__ == "__main__":
    WriteData(0, (1, 69))