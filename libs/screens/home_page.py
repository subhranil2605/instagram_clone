from kivymd.uix.screen import MDScreen
from libs.components.circular_avatar_image import CircularAvatarImage


class HomePage(MDScreen):
    def on_enter(self):
        for i in range(10):
            self.ids.stories.add_widget(CircularAvatarImage(
                avatar='https://images.unsplash.com/photo-1623065691913-e9a650810efd?ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                name="subhranil2605"
            ))
