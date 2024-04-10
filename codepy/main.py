from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from PIL import ImageTk, Image
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from database import *
from plyer import filechooser
from kivy.app import App
from kivy.core.window import Window
import mysql.connector
import bcrypt
import numpy
import cv2 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import os
from kivy.uix.image import Image as KivyImage  
from PIL import Image as PILImage
from keras.models import load_model
model_Train = load_model('my_model.keras')
#dictionary to label all traffic signs class.
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
        "bbcam": "Biển báo cấm",
        "bbhieulenh": "Biển báo hiệu lệnh",
        "bbnguyhiem": "Biển báo nguy hiểm",
        "bbphu": "Biển báo phụ"
        }

# Đường dẫn tới thư mục chứa ảnh của các loại biển báo
image_dir = "D:/HOCTAP/Python/Doanpython/ttbienbao"
current_category = None
previous_categories = []
class TTBienBaoScreen(MDScreen):
    # Định nghĩa các loại biển báo và đường dẫn tới thư mục chứa ảnh của từng loại
    grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
    previous_categories = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.grid_layout.background_color = (0, 0, 0, 1)

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (380, 650)

        for category in categories:
            button = Button(text=categories[category], size_hint=(None, None), size=(150, 50))
            button.bind(on_press=self.on_button_press)
            self.grid_layout.add_widget(button)

        self.add_widget(self.grid_layout)  # Add the GridLayout to the screen

    def on_button_press(self, instance):
        category = None
        for key, value in categories.items():
            if value == instance.text:
                category = key
                break
        if category is not None:
            self.load_category_images(category)
            self.previous_categories.append(category)

    def load_category_images(self, category):
        self.grid_layout.clear_widgets()  # Xóa các widget trong GridLayout
        back_button = Button(text="Quay lại", size_hint=(None, None), size=(150, 50))
        back_button.bind(on_press=self.on_back_button_press)
        self.grid_layout.add_widget(back_button)
        category_dir = os.path.join(image_dir, category)
        if os.path.exists(category_dir):
            for filename in os.listdir(category_dir):
                if filename.endswith(".png"):  # Chỉ tải các tệp tin hình ảnh PNG
                    image_path = os.path.join(category_dir, filename)
                    image_widget = KivyImage(source=image_path, size_hint=(None, None), size=(100, 100))
                    self.grid_layout.add_widget(image_widget)
        else:
            print(f"Thư mục cho loại {category} không tồn tại.")

    def on_back_button_press(self, instance):
        if len(self.previous_categories) > 0:
            self.grid_layout.clear_widgets()
            for category in categories:
                button = Button(text=categories[category], size_hint=(None, None), size=(150, 50))
                button.bind(on_press=self.on_button_press)
                self.grid_layout.add_widget(button)
            self.previous_categories = []

class QuetScreen(MDScreen):
    pass
    # model = None  # Thuộc tính lớp để lưu trữ model

    # def __init__(self, **kwargs):
    #     pass
    #     super().__init__(**kwargs)
    #     self.camera = Camera(resolution=(350, 530), play=True)
    #     self.add_widget(self.camera)

    # def capture_image(self):
    
    #     self.camera.export_to_png(f"IMGt.png")
    #     self.classify('IMGt.png')
            
           

    # def classify(self, file_path):
        
    #     image = Image.open(file_path)
    #     image = image.resize((30, 30))
    #     image = image.convert("RGB")  # Chuyển đổi thành ảnh RGB
    #     image = numpy.expand_dims(image, axis=0)
    #     image = numpy.array(image)
    #     pred_probabilities = QuetScreen.model.predict(image)[0]
    #     pred = pred_probabilities.argmax(axis=-1)
    #     sign = classes[pred+1]
    #     print(sign)
    
class UpLoadHinhScreen(MDScreen):
    
    def open_file_chooser(self):
        # file_chooser = FileChooserIconView()
        # file_chooser.bind(on_submit=self.on_file_choosen)
        # self.add_widget(file_chooser)
        img=filechooser.open_file(on_selection=self.on_file_choosen)
        # Callback được gọi khi file được chọn

    def on_file_choosen(self, selection):
        if selection:
            img_path = selection[0]
            img = cv2.imread(img_path)
            
            if img is not None:  
                image_size_hint_x = 0.65 
                image_size_hint_y = 0.37
                
                target_width = int(App.get_running_app().root.width * image_size_hint_x)
                target_height = int(App.get_running_app().root.height * image_size_hint_y)
                
                resized_img = cv2.resize(img, (target_width, target_height))
                cv2.imwrite(img_path, resized_img)
                
                image_widget = App.get_running_app().root.ids.selected_image
                image_widget.source = img_path
                image_widget.size_hint = (image_size_hint_x, image_size_hint_y)
                self.classify(img_path)
            else:
                print("Failed to load the image:", img_path)
    def classify(self,file_path):
        image = Image.open(file_path)
        image = image.resize((30,30))
        image = numpy.expand_dims(image, axis=0)
        image = numpy.array(image)
        print(image.shape)
        # predict classes
        pred_probabilities = model_Train.predict(image)[0]
        pred = pred_probabilities.argmax(axis=-1)
        sign = classes[pred+1]
        print(sign)   
        label_widget = self.ids.result_label  # Lấy tham chiếu tới MDLabel bằng id
        label_widget.text = sign  # Thiết lập nội dung của MDLabel thành kết quả nhận dạng

class TTAppScreen(MDScreen):
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
                    print("Đăng nhập thành công")
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

class RegisterScreen(Screen):
    def register(self):
        username = self.ids.entry_username_reg.text
        password = self.ids.entry_password_reg.text
        email = self.ids.entry_email_reg.text
        name = self.ids.entry_name_reg.text

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
                insert_query = "INSERT INTO accounts (username, password, email, name) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_query, (username, hashed_password.decode('utf-8'), email, name))
                db_connection.commit()
                self.ids.register_status_label.text = "Đăng ký tài khoản thành công"

            cursor.close()
            db_connection.close()

        except mysql.connector.Error as error:
            print("Lỗi khi thực hiện truy vấn SQL:", error)

class TheLabApp(MDApp):
    def build(self):
        Window.size = (380, 650)
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(name='Login'))
        screen_manager.add_widget(RegisterScreen(name='register'))
        screen_manager.add_widget(MainWidget(name='main'))
        screen_manager.add_widget(TTAppScreen(name='TTApp'))
        screen_manager.add_widget(TTBienBaoScreen(name='TTBienBao'))
        screen_manager.add_widget(QuetScreen(name='Quet'))
        screen_manager.add_widget(UpLoadHinhScreen(name='UpLoadHinh'))
        QuetScreen.model=model_Train
        return screen_manager


TheLabApp().run()