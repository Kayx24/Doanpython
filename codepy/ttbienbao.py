from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Line
from kivy.core.window import Window
import os

classes = {1:'Giới hạn tốc độ (20 km/giờ)',
           2:'Giới hạn tốc độ (30 km/giờ)',
           3:'Giới hạn tốc độ (50 km/giờ)',
           4:'Giới hạn tốc độ (60 km/giờ)', 
           5:'Giới hạn tốc độ (70 km/giờ)',
           6:'Giới hạn tốc độ (80 km/giờ)',
           7:'Hết tốc độ giới hạn (80km/h)', 
           8:'Giới hạn tốc độ (100km/h)',
           9:'Giới hạn tốc độ (120km/h)',
           10:'Không được vượt qua',
           11:'Cấm vượt xe quá 3,5 tấn',
           12:'Quyền ưu tiên tại ngã tư',
           13:'Đường ưu tiên',
           14:'Năng suất',
           15:'Dừng lại',
           16:'Cấm xe cộ', 
           17:'Cấm xe cộ > 3,5 tấn',
           18:'Cấm vào',
           19:'Thận trọng chung',
           20:'Bên trái khúc cua nguy hiểm', 
           21:'Đường cong nguy hiểm bên phải',
           22:'Đường cong đôi',
           23:'Con đường gập ghềnh',
           24:'Đường trơn', 
           25:'Đường bị thu hẹp bên phải',
           26:'Làm đường',
           27:'Tín hiệu giao thông',
           28:'Người đi bộ', 
           29:'Trẻ em băng qua đường',
           30:'Băng qua đường bằng xe đạt',
           31:'Coi chừng băng/tuyết',
           32:'Động vật hoang dã băng qua', 
           33:'Tốc độ cuối + giới hạn vượt',
           34:'Rẽ phải về phía trước',
           35:'Rẽ trái phía trước',
           36:'Chỉ ở phía trước', 
           37:'Đi thẳng hoặc sang phải',
           38:'Đi thẳng hoặc sang trái',
           39:'Giữ bên phải',
           40:'Tiếp tục rời đi',    
           41:'Bùng binh bắt buộc',
           42:'Kết thúc không vượt qua',
           43:'cấm vượt xe > 3,5 tấn' }

image_dir = "D:/HOCTAP/Python/Doanpython/Meta"

class BorderGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(BorderGridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = 10
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        
    def draw_border(self):
        with self.canvas.after:
            Color(1, 0, 0, 1)  # Màu viền đỏ
            Line(rectangle=(self.x, self.y, self.width, self.height), width=2)

class TTbienbao(App):
    def build(self):
        root = ScrollView()
        grid_layout = BorderGridLayout()

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (380, 650)

        for i in range(1, len(classes) + 1):
            image_path = os.path.join(image_dir, f"{i-1}.png")
            image = Image(source=image_path, size_hint=(None, None), size=(100, 100))
            label_text = classes[i]
            label = Label(text=label_text, color=(0, 0, 0, 1), size_hint_y=None, height=30)
            
            grid_layout.add_widget(image)
            grid_layout.add_widget(label)
        
        grid_layout.draw_border() 

        root.add_widget(grid_layout)

        return root

if __name__ == "__main__":
    TTbienbao().run()
