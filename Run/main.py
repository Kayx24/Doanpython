from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
from kivymd.uix.button import MDFlatButton
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from PIL import ImageTk, Image
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from database import *
from plyer import filechooser
from kivy.app import App
from kivy.core.window import Window
from database import connect_to_database
from kivy.uix.button import Button
from kivy.uix.label import Label
import os
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

import mysql.connector
import bcrypt
import numpy
import cv2
import time
from kivyauth.google_auth import initialize_google , login_google , logout_google
from user import User
from keras.models import load_model
model_Train = load_model('my_model.keras')
#dictionary to label all traffic signs class.
file_p_Scan=None

classes = { 1: 'Giới hạn tốc độ (20km/h)',
2: 'Giới hạn tốc độ (30km/h)',
3: 'Giới hạn tốc độ (50km/h)',
4: 'Giới hạn tốc độ (60km/h)',
5: 'Giới hạn tốc độ (70km/h)',
6: 'Giới hạn tốc độ (80km/h)',
7: 'Kết thúc giới hạn tốc độ (80km/h)',
8: 'Giới hạn tốc độ (100km/h)',
9: 'Giới hạn tốc độ (120km/h)',
10: 'Cấm vượt',
11: 'Cấm vượt xe trọng tải trên 3.5 tấn',
12: 'Ưu tiên ở giao lộ',
13: 'Đường ưu tiên',
14: 'Nhường đường',
15: 'Dừng lại',
16: 'Cấm xe',
17: 'Cấm xe trọng tải trên 3.5 tấn',
18: 'Cấm đi',
19: 'Chú ý chung',
20: 'Nguy hiểm ngoặc vòng bên trái',
21: 'Nguy hiểm ngoặc vòng bên phải',
22: 'Nguy hiểm ngoặc vòng kép',
23: 'Đường xấu',
24: 'Đường trơn trượt',
25: 'Đường hẹp bên phải',
26: 'Công trường',
27: 'Đèn giao thông',
28: 'Người đi bộ',
29: 'Đường gặp người đi bộ',
30: 'Đường gặp xe đạp',
31: 'Cẩn thận băng/giá lạnh',
32: 'Gặp động vật hoang dã',
33: 'Kết thúc giới hạn tốc độ và cấm vượt',
34: 'Rẽ phải phía trước',
35: 'Rẽ trái phía trước',
36: 'Chỉ được đi thẳng',
37: 'Đi thẳng hoặc rẽ phải',
38: 'Đi thẳng hoặc rẽ trái',
39: 'Luôn đi bên phải',
40: 'Luôn đi bên trái',
41: 'Vòng xuyến bắt buộc',
42: 'Kết thúc cấm vượt',
43: 'Kết thúc cấm vượt xe trọng tải trên 3.5 tấn'}


categories = {
    "bbcam": ("Biển báo cấm", ["Giới hạn tốc độ (20km/h)",
                               "Giới hạn tốc độ (30km/h)",
                               'Cấm vượt xe trọng tải trên 3.5 tấn',
                               'Dừng lại',
                               'Cấm xe',
                               'Cấm xe trọng tải trên 3.5 tấn',
                               'Cấm đi',
                               "Giới hạn tốc độ (50km/h)",
                               'Giới hạn tốc độ (60km/h)',
                               'Giới hạn tốc độ (70km/h)',
                               'Giới hạn tốc độ (80km/h)',
                               'Giới hạn tốc độ (100km/h)',
                               'Giới hạn tốc độ (120km/h)',
                               'Cấm vượt'
                               ]),
    
    "bbhieulenh": ("Biển báo hiệu lệnh", [ 'Rẽ phải phía trước',
                                            'Rẽ trái phía trước',
                                            'Chỉ được đi thẳng',
                                            'Đi thẳng hoặc rẽ phải',
                                            'Đi thẳng hoặc rẽ trái',
                                            'Luôn đi bên phải',
                                            'Luôn đi bên trái',
                                            ]),
    
    "bbnguyhiem": ("Biển báo nguy hiểm", ['Ưu tiên ở giao lộ',
                                        'Nhường đường',
                                        'Chú ý chung',
                                        'Nguy hiểm ngoặc vòng trái',
                                        'Nguy hiểm ngoặc vòng phải',
                                        'Nguy hiểm ngoặc vòng kép',
                                        'Đường xấu',
                                        'Đường trơn trượt',
                                        'Đường hẹp bên phải',
                                        'Công trường',
                                        'Đèn giao thông',
                                        'Người đi bộ',
                                        'Đường gặp người đi bộ',
                                        'Đường gặp xe đạp',
                                        'Cẩn thận băng/giá lạnh',
                                        'Gặp động vật hoang dã',
]),
    
    "bbphu": ("Biển báo phụ", ['Kết thúc giới hạn tốc độ (80km/h)',
                                'Hết giới hạn tốc độ và cấm vượt',
                                'Kết thúc cấm vượt',
                                'Kết thúc cấm vượt xe trọng tải >3,5 tấn'
]),
    
    "bbchidan": ("Biển báo chỉ dẫn", ['Đường ưu tiên'
]),
    "bbvachkeduong" :("Biển báo vạch kẻ đường", ['Đi bộ qua đường',
                                                 'vạch phân chia 2 chiều xe chạy',
                                                 'vạch chia 2 chiều xe chạy ngược chiều',
                                                 'Phân chia các làn cùng chiều ',
                                                 'vị trí dừng xe công cộng'
    ])
    }

# Directory path to the images of each category
image_dir = "D:/HOCTAP/Python/Doanpython/ttbienbao"



class TTBienBaoScreen(Screen):
    def open_nav_drawer(instance):
        global user
        instance.ids.nav_drawer.set_state("open")
        instance.ids.hoten.title="Chào "+user.hoten
        instance.ids.label_solanquettrongngay.text="Số lượt quét trong ngày: "+str(user.soluotquettrongngay)
        instance.ids.label_tongsolanquet.text="Tổng lượt quét: "+str(user.tongluotquet)
        if user.vip==1:
            
            instance.ids.vip.text="Bạn là VIP <3"
        else:
            instance.ids.vip.text="Hãy là thành viên VIP!"
    def Cam(self):
        print("btn_click_TTCaNhan")
        self.manager.current = 'bienbao'

    def btn_click_Menu(self):
        print("btn_click_Menu")

    def btn_click_Quet(self):
        print("btn_click_LSTim")
        
class bienbaoScreen(MDScreen):
    def on_button_press(self, instance):
        category = None
        for key, value in categories.items():
            if value[0] == instance.text:
                category = key
                break
        if category is not None:
            self.load_category_images(category)
            self.previous_categories.append(category)

    def load_category_images(self, category):
        layout = self.root.ids.layout
        layout.clear_widgets()
        
        back_button = TTbienbaoButton(text="Quay lại")
        back_button.bind(on_press=self.on_back_button_press)
        layout.add_widget(back_button)
        
        category_name, signs = categories[category]
        
        # Tạo nhãn cho tên loại biển báo
        category_label = Label(text=category_name)
        layout.add_widget(category_label)

        category_dir = os.path.join(image_dir, category)
        if os.path.exists(category_dir):
            for filename, sign in zip(os.listdir(category_dir), signs):
                if filename.endswith(".png"): 
                    image_path = os.path.join(category_dir, filename)
                    
                    image_label = ImageLabel(image_path=image_path, label_text=sign)
                    layout.add_widget(image_label)
        else:
            error_label = Label(text=f"Thư mục cho loại {category} không tồn tại.")
            layout.add_widget(error_label)
   



class TTbienbaoButton(Button):
    pass
class ImageLabel(BoxLayout):
    image_path = StringProperty('')
    label_text = StringProperty('')

class QuetScreen(MDScreen):
    pass
    # def open_nav_drawer(instance):
    #     global user
    #     instance.ids.nav_drawer.set_state("open")
    #     instance.ids.hoten.title="Chào "+user.hoten
    #     instance.ids.label_solanquettrongngay.text="Số lượt quét trong ngày: "+str(user.soluotquettrongngay)
    #     instance.ids.label_tongsolanquet.text="Tổng lượt quét: "+str(user.tongluotquet)
    #     if user.vip==1:
    #         instance.ids.vip.text="Bạn là VIP <3"
    #     else:
    #         instance.ids.vip.text="Hãy là thành viên VIP!"
    

    # def __init__(self, **kwargs):
    #     pass
    #     super().__init__(**kwargs)
    #     self.camera = Camera(resolution=(350, 530), play=True)
    #     self.add_widget(self.camera)

    # def capture_image(self):
    #     tongluotquet=user.tongluotquet+1
    #     username=user.username
    #     soluotquettrongngay=user.soluotquettrongngay+1
    #     print("so luot quet trong ngay:",soluotquettrongngay)
    #     print("tong quet:",tongluotquet)
    #     print(username)    
    #     if soluotquettrongngay<=100:
    #         try:
    #             self.camera.export_to_png(f"history/IMG_{user.username}_{tongluotquet}.png")
    #             db_connection = connect_to_database()
    #             cursor = db_connection.cursor()
    #             sql_query = "UPDATE accounts SET soluotquettrongngay = %s, tongluotquet = %s WHERE username = %s" 
    #             values =(soluotquettrongngay,tongluotquet,username)
    #             cursor.execute(sql_query, values)
    #             db_connection.commit()
    #             user.soluotquettrongngay=soluotquettrongngay
    #             user.tongluotquet=tongluotquet
    #             global file_p_Scan
    #             file_p_Scan=(f"history/IMG_{user.username}_{tongluotquet}.png")
    #             self.manager.current = 'UpLoadHinh' 
    #         except mysql.connector.Error as error:
    #             print("Lỗi khi thực hiện truy vấn SQL:", error)
    #     else:
    #         print("nap vip di em")
  
class UpLoadHinhScreen(MDScreen):
    def on_enter(self, *args):
        super().on_enter(*args)
        self.on_file_quetScreen()
    def open_nav_drawer(instance):
        global user        
        instance.ids.nav_drawer.set_state("open")
        instance.ids.hoten.title="Chào "+user.hoten
        instance.ids.label_solanquettrongngay.text="Số lượt quét trong ngày: "+str(user.soluotquettrongngay)
        instance.ids.label_tongsolanquet.text="Tổng lượt quét: "+str(user.tongluotquet)
        if user.vip==1:
            instance.ids.vip.text="Bạn là VIP <3"
        else:
            instance.ids.vip.text="Hãy là thành viên VIP!"
    def open_file_chooser(self):
        # file_chooser = FileChooserIconView()
        # file_chooser.bind(on_submit=self.on_file_choosen)
        # self.add_widget(file_chooser)
        img=filechooser.open_file(on_selection=self.on_file_choosen)
        
        # Callback được gọi khi file được chọn

    def on_file_choosen(self, selection):
        if selection:
            img_path = selection[0]
            print(img_path)
            img = cv2.imread(img_path)
            
            if img is not None:
                self.ids.selected_image.source = img_path
                self.ids.selected_image.reload()
                self.classify(img_path)
            else:
                print("Failed to load the image:", img_path)
    def on_file_quetScreen(self):
            global file_p_Scan
            
            if file_p_Scan is not None:
                self.ids.selected_image.source = file_p_Scan
                self.ids.selected_image.reload()
                self.classify(file_p_Scan)
            else:
                
                file_path_scan=('Images\Holo _ Gyate Gyate _ Ohayou.jpg')
                self.ids.selected_image.source = file_path_scan
                label_widget = self.ids.result_label  # Lấy tham chiếu tới MDLabel bằng id
                label_widget.text = "Cho xinn tấm ảnh đii:3"
    def classify(self, file_path):
        image = Image.open(file_path)
        image = image.resize((30, 30))
        image = numpy.array(image)
        
        # Chuyển đổi từ RGBA sang RGB
        if image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        
        image = numpy.expand_dims(image, axis=0)
        image = image.astype(numpy.float32)
        
        # predict classes
        pred_probabilities = model_Train.predict(image)[0]
        pred = pred_probabilities.argmax(axis=-1)
        sign = classes[pred+1]
        print(sign)   
        label_widget = self.ids.result_label
        label_widget.text = sign



class TTAppScreen(MDScreen):
    def open_nav_drawer(instance):
        global user
        instance.ids.nav_drawer.set_state("open")
        instance.ids.hoten.title="Chào "+user.hoten
        instance.ids.label_solanquettrongngay.text="Số lượt quét trong ngày: "+str(user.soluotquettrongngay)
        instance.ids.label_tongsolanquet.text="Tổng lượt quét: "+str(user.tongluotquet)
        if user.vip==1:
            instance.ids.vip.text="Bạn là VIP <3"
        else:
            instance.ids.vip.text="Hãy là thành viên VIP!"
    def on_press(self):
        self.icon = "Images/onpress.png"
        print("1")
        pass
        # function onclick

    def on_release(self):
        self.icon = "Images/homeIcon.png"
        print("2")
        pass
        
class MainWidget(MDScreen):
    
    def on_enter(self, *args):
        super().on_enter(*args)
        global file_p_Scan
        file_p_Scan=None
        print(file_p_Scan)
        self.close_nav_drawer()

    def close_nav_drawer(self):
        self.ids.nav_drawer.set_state("close")

    def open_nav_drawer(instance):
        global user
        instance.ids.nav_drawer.set_state("open")
        instance.ids.hoten.title="Chào "+user.hoten
        instance.ids.label_solanquettrongngay.text="Số lượt quét trong ngày: "+str(user.soluotquettrongngay)
        instance.ids.label_tongsolanquet.text="Tổng lượt quét: "+str(user.tongluotquet)
        if user.vip==1:
            instance.ids.vip.text="Bạn là VIP <3"
        else:
            instance.ids.vip.text="Hãy là thành viên VIP!"

        
    manager = None  # Thuộc tính để lưu trữ đối tượng ScreenManager

    def btn_click_TTCaNhan(self):
        print("btn_click_TTCaNhan")

    def btn_click_Menu(self):
        print("btn_click_Menu")

    def btn_click_Tim(self):
        print("btn_click_Tim")

    def btn_click_UploadHinh(self):
        print("btn_click_UploadHinh")
        self.manager.current = 'UpLoadHinh'  # Chuyển đến màn hình "UploadHinh"


    def btn_click_TTBienBao(self):
        self.manager.current='TTBienBao'

    def btn_click_TTApp(self):
        print("btn_click_TTApp")
        self.manager.current = 'TTApp'  # Chuyển đến màn hình "TTApp"

    def btn_click_LSTim(self):
        print("btn_click_LSTim")

    def btn_click_Quet(self):
        print("btn_click_Quet")
        self.manager.current = 'Quet'  # Chuyển đến màn hình "TTApp"
       
class Main_login(Screen):
    pass

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
                    self.show_dialog_login("Đăng nhập thành công")
                    global user
                    user=User(result[4],result[5],result[6],result[7],result[8],result[1],result[2],result[3])
                    self.manager.current = 'main'
                else:
                    self.show_dialog_login("Tên đăng nhập hoặc mật khẩu không chính xác. Vui lòng đăng nhập lại.")
            else:
                self.show_dialog_login("Tên đăng nhập hoặc mật khẩu không chính xác. Vui lòng đăng nhập lại.")

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)

    def show_dialog_login(self, message):
        self.dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.close_dialog_login
                )
            ]
        )
        self.dialog.open()

    def close_dialog_login(self, *args):
       # App.get_running_app().root.current = 'login'
        self.dialog.dismiss()

class RegisterScreen(Screen):
    def register(self):
        username = self.ids.entry_username_reg.text.strip()  # Xóa các khoảng trắng thừa
        password = self.ids.entry_password_reg.text.strip()

        # Kiểm tra xem có bất kỳ trường nào trống không
        if not username or not password:
            self.show_try_again_dialog("Vui lòng điền đầy đủ thông tin.")
            return

        try:
            db_connection = connect_to_database()
            cursor = db_connection.cursor()

            # Kiểm tra xem tên người dùng đã tồn tại chưa
            check_username_query = "SELECT * FROM accounts WHERE username = %s"
            cursor.execute(check_username_query, (username,))
            existing_username = cursor.fetchone()

        

            if existing_username:
                self.show_try_again_dialog("Tên người dùng đã tồn tại. Vui lòng chọn tên khác.")
            else:
                # Nếu không có tên người dùng hoặc email trùng lặp, thêm tài khoản mới vào cơ sở dữ liệu
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                insert_query = "INSERT INTO accounts (username, password) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, hashed_password.decode('utf-8')))
                db_connection.commit()
                self.show_dialog("Đăng ký tài khoản thành công")

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)

    def show_dialog(self, message):
        self.dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.close_dialog
                )
            ]
        )
        self.dialog.open()

    def show_try_again_dialog(self, message):
        self.dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.clear_username_field
                )
            ]
        )
        self.dialog.open()

    def close_dialog(self, *args):
        App.get_running_app().root.current = 'Login'
        self.dialog.dismiss()

    def clear_username_field(self, *args):
        # Xóa nội dung của trường nhập liệu tên
        self.ids.entry_username_reg.text = ""
        self.dialog.dismiss()


class TheLabApp(MDApp):
    
    def login1(self):
        login_google()
        
    def show_try_again_dialog(self, message):
        self.dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.clear_username_field
                )
            ]
        )
        self.dialog.open()
    def clear_username_field(self, *args):
        # Xóa nội dung của trường nhập liệu tên
        self.ids.entry_username_reg.text = ""
        self.dialog.dismiss()
    def close_dialog(self, *args):
        App.get_running_app().root.current = 'Login'
        self.dialog.dismiss()

    def after_login(self, name, email, password):
        print("Tên của bạn là " + name)
        print("Email: " + email)
        # Kiểm tra xem email đã được sử dụng chưa
        try:
            db_connection = connect_to_database()
            cursor = db_connection.cursor()
            sql_query = "SELECT * FROM accounts WHERE email = %s"
            cursor.execute(sql_query, (email,))
            result = cursor.fetchone()
            try:
                if result!=None:
                    global user
                    user=User(result[4],result[5],result[6],result[7],result[8],result[1],result[2],result[3])
                    self.manager.current = "main"
                else:
                    # Nếu không có tên người dùng hoặc email trùng lặp, thêm tài khoản mới vào cơ sở dữ liệu
                    insert_query = "INSERT INTO accounts (hoten, username, email) VALUES (%s, %s, %s)"
                    cursor.execute(insert_query, (name,email,email))
                    db_connection.commit()
                    self.show_dialog("Đăng ký tài khoản thành công")
                    user=User(result[4],result[5],result[6],result[7],result[8],result[1],result[2],result[3])
                    self.manager.current = "main"
            except:
                print("loi re")

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)
        # Chuyển đến màn hình chính sau khi đăng nhập
        self.manager.transition.direction = "left"
        self.manager.current = "main"
    def error_listener(self):
        print("Đăng nhập không thành công")

    def logout(self):
        logout_google()

    def after_logout(self):
        self.manager.current = "right"
        self.manager.current = "Login"
    
    
    def build(self):
        Window.size = (380, 650)
        self.title="Nhận diện biển báo giao thông"
        client_id=open("D:\HOCTAP\Python\Doanpython\Run\client_id.txt")
        client_secret=open("D:\HOCTAP\Python\Doanpython\Run\client_secret.txt")
        initialize_google(self.after_login , self.error_listener , client_id.read() , client_secret.read())
        screen_manager = ScreenManager()
        TheLabApp.manager = screen_manager
        screen_manager.add_widget(Main_login(name='Main_login'))
        screen_manager.add_widget(LoginScreen(name='Login'))
        screen_manager.add_widget(RegisterScreen(name='register'))
        screen_manager.add_widget(MainWidget(name='main'))
        screen_manager.add_widget(TTAppScreen(name='TTApp'))
        screen_manager.add_widget(TTBienBaoScreen(name='TTBienBao'))
        screen_manager.add_widget(QuetScreen(name='Quet'))
        screen_manager.add_widget(UpLoadHinhScreen(name='UpLoadHinh'))
        screen_manager.add_widget(bienbaoScreen(name = 'bienbao'))
        QuetScreen.model=model_Train
        return screen_manager


TheLabApp().run()