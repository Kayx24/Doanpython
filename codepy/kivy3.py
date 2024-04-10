from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer

from kivy.properties import ListProperty

from plyer import filechooser

Window.size=(380,680)

Builder.load_file('bg copy.kv')

class MyLayout(MDScreen):
    def open_file_chooser(self):
        # file_chooser = FileChooserIconView()
        # file_chooser.bind(on_submit=self.on_file_choosen)
        # self.add_widget(file_chooser)
        filechooser.open_file(on_selection=self.on_file_choosen)

        # Callback được gọi khi file được chọn

    def on_file_choosen(self, selection):
        if selection:
            App.get_running_app().root.ids.selected_image.source = selection[0]






class AwesomeApp(MDApp):
    def build(self):
        return MyLayout()

if __name__=="__main__":
    AwesomeApp().run()