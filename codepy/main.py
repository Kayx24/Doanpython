from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera

import time

class TTAppScreen(Screen):
    pass
class TTBienBaoScreen(Screen):

    def btn_click_TTCaNhan(self):
        print("btn_click_TTCaNhan")

    def btn_click_Menu(self):
        print("btn_click_Menu")

    def btn_click_Quet(self):
        print("btn_click_LSTim")

class QuetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = Camera(resolution=(640, 480), play=True)
        self.add_widget(self.camera)

    def capture_image(self):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png(f"IMG_{timestr}.png")
        print("Đã chụp ảnh")
    
    
class MainWidget(Widget):
    manager = None  # Thuộc tính để lưu trữ đối tượng ScreenManager

    def btn_click_TTCaNhan(self):
        print("btn_click_TTCaNhan")

    def btn_click_Menu(self):
        print("btn_click_Menu")

    def btn_click_Tim(self):
        print("btn_click_Tim")

    def btn_click_UploadHinh(self):
        print("btn_click_UploadHinh")

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



class TheLabApp(App):
    def build(self):
        Window.size = (380, 650)
        screen_manager = ScreenManager()
        main_screen = Screen(name='main')
        main_widget = MainWidget()
        main_widget.manager = screen_manager  # Truyền đối tượng ScreenManager
        main_screen.add_widget(main_widget)
        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(TTAppScreen(name='TTApp'))
        screen_manager.add_widget(TTBienBaoScreen(name='TTBienBao'))
        screen_manager.add_widget(QuetScreen(name='Quet'))
        return screen_manager


TheLabApp().run()