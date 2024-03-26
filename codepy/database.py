import mysql.connector

def connect_to_database():
    try:
        # Kết nối đến cơ sở dữ liệu MySQL
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Thay bằng mật khẩu của bạn nếu có
            database="pythonbienbao"
        )
        
        print("Kết nối đến cơ sở dữ liệu thành công")
        return db_connection
        
    except mysql.connector.Error as error:
        print("Lỗi khi kết nối đến cơ sở dữ liệu:", error)
        return None

def create_table_accounts(cursor):
    # Thực thi truy vấn SQL để tạo bảng accounts nếu chưa tồn tại
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)