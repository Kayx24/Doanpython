from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from register import RegisterScreen
from database import connect_to_database
import mysql.connector
import bcrypt
from kivy.uix.image import Image

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_login_layout()

    def create_login_layout(self):
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        img = Image(source="bienbao.png", size_hint=(None, None), size=(150,150),pos_hint={'center_x': 0.5, 'top':2 })
        layout.add_widget(img)

        with layout.canvas.before:
            Color(1, 1, 1, 1) 
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        form_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.label_username = Label(text="Username:", font_size=16, size_hint_x=None, width=100, color=(0, 0, 0, 1))
        self.entry_username = TextInput(font_size=16, size_hint_x=None)

        self.label_password = Label(text="Password:", font_size=16, size_hint_x=None, width=100, color=(0, 0, 0, 1))
        self.entry_password = TextInput(password=True, font_size=16, size_hint_x=None)

        form_layout.add_widget(self.label_username)
        form_layout.add_widget(self.entry_username)
        form_layout.add_widget(self.label_password)
        form_layout.add_widget(self.entry_password)

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, size_hint_x=0.5, height=50)

        self.button_login = Button(text="Đăng nhập", font_size=16,background_color=(0,1,2,1))
        self.button_login.bind(on_press=self.login)

        self.button_register = Button(text="Đăng ký", font_size=16,background_color=(0,1,2,1))
        self.button_register.bind(on_press=self.switch_to_register_layout)

        button_layout.add_widget(self.button_login)
        button_layout.add_widget(self.button_register)

        self.login_status_label = Label(text="", font_size=16, size_hint_y=None, height=30)

        layout.add_widget(form_layout)
        layout.add_widget(button_layout)
        layout.add_widget(self.login_status_label)

        self.add_widget(layout)

    def switch_to_register_layout(self, instance):
        self.manager.current = 'register'

    def login(self, instance):
        username = self.entry_username.text
        password = self.entry_password.text

        try:
            db_connection = connect_to_database()
            cursor = db_connection.cursor()
            sql_query = "SELECT * FROM accounts WHERE username = %s"
            cursor.execute(sql_query, (username,))
            result = cursor.fetchone()

            if result:
                hashed_password_from_db = result[2] 
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db.encode('utf-8')):
                    self.login_status_label.text = "Đăng nhập thành công"
                else:
                    self.login_status_label.text = "Đăng nhập thất bại"
            else:
                self.login_status_label.text = "Đăng nhập thất bại"

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)

    def on_parent(self, instance, value):
        if value is None:
            Window.unbind(on_resize=self.on_window_resize)
        else:
            Window.bind(on_resize=self.on_window_resize)
            self.on_window_resize(Window, Window.width, Window.height)


    def on_window_resize(self, instance, width, height):
        self.entry_username.width = width / 2
        self.entry_password.width = width / 2

class LoginApp(App):
    def build(self):
        self.title = "Đăng nhập"
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (400, 400)
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))

        return sm

if __name__ == "__main__":
    LoginApp().run()
