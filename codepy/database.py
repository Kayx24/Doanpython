import mysql.connector

def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pythonbienbao"
        )
        
        print("Kết nối đến cơ sở dữ liệu thành công")
        return db_connection
        
    except mysql.connector.Error as error:
        print("Lỗi khi kết nối đến cơ sở dữ liệu:", error)
        return None

def create_table_accounts(cursor):
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)