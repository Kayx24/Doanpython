from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import os

# Define the categories and the directory path containing the images for each category
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

class TTbienbao(App):
    current_category = None
    previous_categories = []

    def build(self):
        self.layout = GridLayout(cols=2, spacing=20, size_hint_y=None, padding=(0, 150, 0, 0))
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.layout)
        
        for category_name, (category_text, _) in categories.items():
            button = Button(text=category_text, size_hint_y=None, height=150,
                            background_color=(0.2, 0.6, 0.9, 1), color=(1, 1, 1, 1), font_size=16,
                            pos_hint={'center_x': 0.5})
            button.bind(on_press=self.on_button_press)
            self.layout.add_widget(button)
        
        return scroll_view

 

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
        self.layout.clear_widgets()
        
        back_button = Button(text="Quay lại", size_hint_y=None, height=50,
                            background_color=(0.9, 0.2, 0.2, 1), color=(1, 1, 1, 1), font_size=16)
        back_button.bind(on_press=self.on_back_button_press)
        self.layout.add_widget(back_button)
        
        category_name, signs = categories[category]
        
        # Tạo nhãn cho tên loại biển báo
        category_label = Label(text=category_name, size_hint_y=None, height=50, color=(0, 0, 0, 1))
        self.layout.add_widget(category_label)

        category_dir = os.path.join(image_dir, category)
        if os.path.exists(category_dir):
            for filename, sign in zip(os.listdir(category_dir), signs):  # Sử dụng hàm zip để kết hợp các tên biển báo và hình ảnh
                if filename.endswith(".png"): 
                    image_path = os.path.join(category_dir, filename)
                    
                    image_widget = Image(source=image_path, size_hint_y=None, height=100)
                    self.layout.add_widget(image_widget)
                    
                    # Thêm thông tin về biển báo dưới hình ảnh
                    sign_label = Label(text=sign, size_hint_y=None, height=50, color=(0, 0, 0, 1))
                    self.layout.add_widget(sign_label)
        else:
            error_label = Label(text=f"Thư mục cho loại {category} không tồn tại.", color=(0, 0, 0, 1))
            self.layout.add_widget(error_label)


    def on_back_button_press(self, instance):
        if len(self.previous_categories) > 0:
            layout = self.root.children[0]
            layout.clear_widgets()
            for category_name, (category_text, _) in categories.items():
                button = Button(text=category_text, size_hint_y=None, height=150,
                                background_color=(0.2, 0.6, 0.9, 1), color=(1, 1, 1, 1), font_size=16)
                button.bind(on_press=self.on_button_press)
                layout.add_widget(button)
            self.previous_categories = []

if __name__ == "__main__":
    Window.clearcolor = (1, 1, 1, 1)
    Window.size = (380, 650)
    TTbienbao().run()
