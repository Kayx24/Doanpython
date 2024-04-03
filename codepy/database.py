import mysql.connector

def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Thay bằng mật khẩu cơ sở dữ liệu của bạn
            database="pythonbienbao"
        )

        if db_connection.is_connected():
            print("Kết nối đến cơ sở dữ liệu thành công")
            return db_connection
        else:
            print("Kết nối đến cơ sở dữ liệu không thành công")
            return None

    except mysql.connector.Error as error:
        print("Lỗi khi kết nối đến cơ sở dữ liệu:", error)
        return None

def create_table_accounts(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        """)
        print("Table 'accounts' created successfully.")
    except mysql.connector.Error as error:
        print("Error creating table 'accounts':", error)


if __name__ == "__main__":
    connection = connect_to_database()
    if connection is not None:
        cursor = connection.cursor()
        create_table_accounts(cursor)
        connection.close()
