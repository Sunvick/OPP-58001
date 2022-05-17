import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ichil\Downloads\Database2.accdb')
    print("Connected to a Database")

    Fullname = "Sunvick A. Gencianeo"
    Assignment = 94
    Laboratory = 91
    Quiz = 93
    Exam = 91
    user_id =10

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ?, Assignment = ?, Laboratory = ?, Quiz = ?, Exam = ? WHERE id = ?', (Fullname, Assignment, Laboratory, Quiz, Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
