import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ichil\Downloads\Database2.accdb')
    print("Connected to a Database")