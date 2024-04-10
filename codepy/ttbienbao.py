from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import os

# Định nghĩa các loại biển báo và đường dẫn tới thư mục chứa ảnh của từng loại
categories = {
    "bbcam": "Biển báo cấm",
    "bbhieulenh": "Biển báo hiệu lệnh",
    "bbnguyhiem": "Biển báo nguy hiểm",
    "bbphu": "Biển báo phụ"
}

# Đường dẫn tới thư mục chứa ảnh của các loại biển báo
image_dir = "D:/HOCTAP/Python/Doanpython/ttbienbao"

class TTbienbao(App):
    current_category = None
    previous_categories = []

    def build(self):
        self.grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.grid_layout.background_color = (0, 0, 0, 1)

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (380, 650)

        for category in categories:
            button = Button(text=categories[category], size_hint=(None, None), size=(150, 50))
            button.bind(on_press=self.on_button_press)
            self.grid_layout.add_widget(button)
        
        return self.grid_layout

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
                    image_widget = Image(source=image_path, size_hint=(None, None), size=(100, 100))
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

if __name__ == "__main__":
    TTbienbao().run()
