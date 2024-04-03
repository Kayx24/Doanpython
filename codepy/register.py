from kivy.uix.screenmanager import Screen
from database import connect_to_database
import mysql.connector
import bcrypt
from kivy.lang import Builder

Builder.load_file('register.kv')

class RegisterScreen(Screen):
    def register(self):
        username = self.ids.entry_username_reg.text
        password = self.ids.entry_password_reg.text
        email = self.ids.entry_email_reg.text

        try:
            db_connection = connect_to_database()
            cursor = db_connection.cursor()

            check_query = "SELECT * FROM accounts WHERE username = %s"
            cursor.execute(check_query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                self.ids.register_status_label.text = "Tên người dùng đã tồn tại. Vui lòng chọn tên khác."
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                insert_query = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (username, hashed_password.decode('utf-8'), email))
                db_connection.commit()
                self.ids.register_status_label.text = "Đăng ký tài khoản thành công"

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)
