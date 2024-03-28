from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from database import connect_to_database
import mysql.connector
import bcrypt


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_register_layout()

    def create_register_layout(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        self.label_username_reg = Label(text="Username:", font_size=16, size_hint_x=None, width=100)
        self.entry_username_reg = TextInput(font_size=16)

        self.label_password_reg = Label(text="Password:", font_size=16, size_hint_x=None, width=100)
        self.entry_password_reg = TextInput(password=True, font_size=16)

        self.label_email_reg = Label(text="Email:", font_size=16, size_hint_x=None, width=100)
        self.entry_email_reg = TextInput(font_size=16)

        form_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        form_layout.add_widget(self.label_username_reg)
        form_layout.add_widget(self.entry_username_reg)
        form_layout.add_widget(self.label_password_reg)
        form_layout.add_widget(self.entry_password_reg)
        form_layout.add_widget(self.label_email_reg)
        form_layout.add_widget(self.entry_email_reg)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        self.button_register_reg = Button(text="Đăng ký", font_size=16)
        self.button_register_reg.bind(on_press=self.register)

        self.button_back = Button(text="Quay lại", font_size=16)
        self.button_back.bind(on_press=self.switch_to_login_layout)

        button_layout.add_widget(self.button_register_reg)
        button_layout.add_widget(self.button_back)

        self.register_status_label = Label(text="", font_size=16, size_hint_y=None, height=30)

        layout.add_widget(form_layout)
        layout.add_widget(button_layout)
        layout.add_widget(self.register_status_label)

        self.add_widget(layout)

    def switch_to_login_layout(self, instance):
        self.manager.current = 'login'

    def register(self, instance):
        username = self.entry_username_reg.text
        password = self.entry_password_reg.text
        email = self.entry_email_reg.text

        try:
            db_connection = connect_to_database()
            cursor = db_connection.cursor()

            check_query = "SELECT * FROM accounts WHERE username = %s"
            cursor.execute(check_query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                self.register_status_label.text = "Tên người dùng đã tồn tại. Vui lòng chọn tên khác."
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                insert_query = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (username, hashed_password.decode('utf-8'), email))
                db_connection.commit()
                self.register_status_label.text = "Đăng ký tài khoản thành công"

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)
