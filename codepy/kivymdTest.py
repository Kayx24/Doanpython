from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.textfield import textfield
from kivymd.uix.button import MDTextButton
from kivymd.uix.bottomnavigation import bottomnavigation
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.scrollview import ScrollView

class ListDemo(MDScreen):
    pass

kv= '''
    MDScreen:
        ScrollView:
            MDList:
                id: container
'''
class Demo(MDScreen):
    pass

#Tạo class nút home
class HomeButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = "Images/homeIcon.png"
        self.size_hint = 0.05, 0.05
        self.pos_hint = {'center_x':0.5, 'center_y': 0.5}
    def on_press(self):
        self.source = "Images/onpress.png"
        #funtion onclick
    def on_release(self):
        self.source = "Images/homeIcon.png"

KV = '''
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#000000"
                    elevation: 5
                    left_action_items:[["menu", lambda x: nav_drawer.set_state("open")]]

                    #right_action_items:[["magnify", lambda x: none]]
                MDIconButton:
                    id: magnifybutton
                    icon: 'magnify'
                    icon_color: 255,215,0
                    icon_size: "60dp"
                    size_hint: 0.15, 0.1
                    pos_hint: {'center_x':0.9, 'center_y': 0.85}
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint: 0.85, 0.65
                    pos_hint: {'center_x':0.5, 'center_y': 0.45}
                    #md_bg_color: "#e7e4c0"
                    padding: 5
                    spacing: -7
                    Image:
                        source: "Images/Logo.png"
                        size_hint: 3.5, 3.5
                        pos_hint: {'center_x':0.5}
                    Image:
                        source: "Images/memList.png"
                        size_hint: 2.15, 2.15
                        pos_hint: {'center_x':0.5}
                    Image:
                        source: "Images/email.png"
                        size_hint: 1,1
                        pos_hint: {'center_x':0.5}
                # MDFloatingActionButton:
                #     icon: "Images/homeIcon.png"
                #     icon_size: "80sp"
                #     theme_item_color: "Custom"
                #     size_hint: 0.18, 0.1
                #     pos_hint: {'center_x': 0.5, 'center_y':0.1}
                #     background_color: 0,0,0,0
                MDBottomAppBar:
                    id: bottom_appbar
                    md_bg_color: "#e7e4c0"

                    MDFabBottomAppBarButton:
                        id: fab_button
                        icon: "home"
                        theme_bg_color: "Custom"
                        md_bg_color: "#373A22"
                        pos_hint: {'center_x': 0.5}
                    

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0,16,0,16)
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    source:"Images/__ruan_mei_honkai_and_1_more__fe90c2ad3c46efd002abe86229bcdc37.png"
                    title: "Mei dep gai"
                    text: "Meixinhdep@yahoo.com"
                    text_size: 0.07
                    spacing: "10dp"
                    padding: "12dp", 0,0, "50dp"
                MDNavigationDrawerLabel:
                    text: "User" 
                MDNavigationDrawerItem:
                    icon: "star"
                    right_text: ""
                    text_right_color: "#4a4939"
                    text: "Purchase V.I.P"
                MDNavigationDrawerItem:
                    icon: "Images/shareIcon.png"
                    right_text: ""
                    text_right_color: "#4a4939"
                    text: "Share"
                    spacing: "10dp"
                    padding: "10dp",0,0, "30dp"
                MDNavigationDrawerItem:
                    text: "               Log out"
                    align: "center"
                    background_color: 1,0,0,0

        MDNavigationDrawer:
            id: right_nav_drawer
            radius: (0,16,0,16)
                
'''
class MyAppMD(MDApp):
    def build(self):
        self.title = "Frame 5"
        gridLayout = GridLayout(cols = 1)
        # sm = ScreenManager()
        # sm.add_widget(Demo())
        kv = Builder.load_string(KV)
        gridLayout.add_widget(kv)

        #test = Builder.load_string(kv)
        Window.size = (370,680)
        return gridLayout
    # def on_start(self):
    #     for i in range(10):
    #         items = OneLineIconListItem(text = 'Item ' + str(i))
    #         self.root.ids.container.add_widget(items)
    #Chưa dùng 
    def on_press(self):
        self.icon = "Images/onpress.png"
        #function onclick
    def on_release(self):
        self.icon = "Images/homeIcon.png"

MyAppMD().run()


