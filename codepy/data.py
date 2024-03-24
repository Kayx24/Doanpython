import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="",
    database="pythonbienbao"
)

if connection.is_connected:
    print("Ket noi thanh cong")
else:
    print("ket noi that bai")
    
connection.close()