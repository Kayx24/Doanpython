from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from kivy.uix.button import Button
from datatable import DataTable
from database import connect_to_database
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import sqlite3



class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        content = self.ids.scrn_user
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        # Display Products
        thongke_scrn = self.ids.scrn_thong_ke
        thongkes = self.get_thongKe()
        prod_table = DataTable(table=thongkes)
        thongke_scrn.add_widget(prod_table)

    def delete_selected_accounts(self):
        selected_accounts = self.get_selected_accounts()
        if selected_accounts:
            self.delete_non_vip_accounts(selected_accounts)
        else:
            print("Không có tài khoản nào được chọn.")



    def get_selected_accounts(self):
        selected_accounts = []
        # Lặp qua các tài khoản và kiểm tra xem chúng đã được chọn chưa
        for child in self.ids.scrn_users.children:
            if hasattr(child, 'selected') and child.selected:
                selected_accounts.append(child.ids.username_label.text)  # Thêm tên tài khoản vào danh sách
        return selected_accounts


    def delete_non_vip_accounts(self, selected_accounts):
        db_connection = connect_to_database()
        if db_connection is not None:
            cursor = db_connection.cursor()
            try:
                # Xóa các tài khoản không phải VIP được chọn
                placeholders = ','.join(['?'] * len(selected_accounts))
                sql = "DELETE FROM accounts WHERE vip=0 AND username IN ({})".format(placeholders)
                cursor.execute(sql, selected_accounts)
                db_connection.commit()
                print("Đã xóa các tài khoản không phải VIP được chọn thành công!")
            except sqlite3.Error as e:
                print("Lỗi khi xóa tài khoản:", e)
            finally:
                db_connection.close()
        else:
            print("Không thể kết nối đến cơ sở dữ liệu.")


    def get_users(self):
        db_connection = connect_to_database()
        if db_connection is not None:
            cursor = db_connection.cursor()
            _users = OrderedDict()
            _users['user_name'] = {}
            _users['last_name'] = {}
            _users['email'] = {}
            username = []
            email = []
            hoten = []

            sql = 'SELECT * FROM accounts WHERE vip=0'
            cursor.execute(sql)
            users = cursor.fetchall()
            for user in users:
                username.append(user[1])
                email_address = user[3]
                email.append(email_address)
                hoten.append(user[4])

            users_length = len(username)
            idx = 0
            while idx < users_length:
                _users['user_name'][idx] = username[idx]
                _users['last_name'][idx] = hoten[idx]
                _users['email'][idx] = email[idx]
                idx += 1

            db_connection.close()
            return _users
        else:
            return None


    def get_thongKe(self):
        db_connection = connect_to_database()
        if db_connection is not None:
            cursor = db_connection.cursor()
            _thongke = OrderedDict()
            _thongke['vip'] = {}
            _thongke['so_luot_quet_ngay'] = {}
            _thongke['tong_luot_quet'] = {}
            _thongke['so_luot_hai_long'] = {}
            _thongke['so_luot_khong_hai_long'] = {}
            vip = []
            soluotquettrongngay = []
            tongluotquet = []
            soluothailong = []
            soluotkhonghailong = []

            sql = 'SELECT * FROM accounts'
            cursor.execute(sql)
            thongkes = cursor.fetchall()
            for thongke in thongkes:
                vip.append(thongke[5])
                soluotquettrongngay.append(thongke[6])
                tongluotquet.append(thongke[7])
                soluothailong.append(thongke[8])
                soluotkhonghailong.append(thongke[9])
                # vip = user[3]

                # if len(vip) > 10:
                #     vip = vip[:10] + '...'
                # soluothailong.append(vip)
                # soluotkhonghailong.append(user[4])
            users_length = len(vip)
            idx = 0
            while idx < users_length:
                _thongke['vip'][idx] = vip[idx]
                _thongke['so_luot_quet_ngay'][idx] = soluotquettrongngay[idx]
                _thongke['tong_luot_quet'][idx] = tongluotquet[idx]
                _thongke['so_luot_hai_long'][idx] = soluothailong[idx]
                _thongke['so_luot_khong_hai_long'][idx] = soluotkhonghailong[idx]
                idx += 1

            db_connection.close()
            return _thongke
        else:
            return None



    def change_screen(self, instance):
        if instance.text == 'quản lí người dùng':
            self.ids.scrn_mngr.current = 'scrn_user'
        else:
            self.ids.scrn_mngr.current = 'scrn_thong_ke'
            #self.ids.scrn_mngr.current = 'scrn_user'


        # else:
        #     self.ids.scrn_mngr.current = 'scrn_analysis'

class AdminApp(App):
    def build(self):
        #Builder.load_file('admin.kv')
        return AdminWindow()

if __name__ == '__main__':
    AdminApp().run()
