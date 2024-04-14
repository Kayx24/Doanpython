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
