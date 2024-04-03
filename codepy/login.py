from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from database import connect_to_database
import mysql.connector
import bcrypt
from register import *
from main import MainWidget


class LoginScreen(Screen):
    def login(self):
        username = self.ids.entry_username.text
        password = self.ids.entry_password.text

        try:
            db_connection = connect_to_database()
            cursor = db_connection.cursor()
            sql_query = "SELECT * FROM accounts WHERE username = %s"
            cursor.execute(sql_query, (username,))
            result = cursor.fetchone()

            if result:
                hashed_password_from_db = result[2] 
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db.encode('utf-8')):
                    self.ids.login_status_label.text = "Đăng nhập thành công"
                    self.manager.current = 'main'
                else:
                    self.ids.login_status_label.text = "Đăng nhập thất bại"
            else:
                self.ids.login_status_label.text = "Đăng nhập thất bại"

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
        entry_username = self.ids.get('entry_username')
        if entry_username:
            entry_username.width = width / 2
        entry_password = self.ids.get('entry_password')
        if entry_password:
            entry_password.width = width / 2

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
