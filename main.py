from kivymd.app import MDApp
from kivy.lang.builder import Builder

from libs.screens.home_page import HomePage


class InstagramApp(MDApp):
    def build(self):
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')


if __name__ == '__main__':
    InstagramApp().run()
