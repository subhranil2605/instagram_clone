from kivymd.uix.screen import MDScreen

from libs.components.circular_avatar_image import CircularAvatarImage
from libs.components.postcard import PostCard

class HomePage(MDScreen):
    def on_enter(self):
        self.list_stories()
        self.list_post()

    def list_stories(self):
        for i in range(10):
            self.ids.stories.add_widget(CircularAvatarImage(
                avatar='https://images.unsplash.com/photo-1623065691913-e9a650810efd?ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                name="subhranil2605"
            ))

    def list_post(self):
        for i in range(10):
            self.ids.timeline.add_widget(PostCard(
                avatar='https://images.unsplash.com/photo-1623100802758-27f1c893f31f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=334&q=80',
                username='subhranil2605',
                post='https://images.unsplash.com/photo-1623100802758-27f1c893f31f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=334&q=80',
                caption='Create Full Page Scroll Views'
            ))