import json

from kivymd.uix.screen import MDScreen

from libs.components.circular_avatar_image import CircularAvatarImage
from libs.components.postcard import PostCard


class HomePage(MDScreen):
    profile_picture = 'https://images.unsplash.com/photo-1623065691913-e9a650810efd?ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'

    def on_enter(self):
        self.list_stories()
        self.list_post()

    def list_stories(self):
        with open('assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar=data[name]['avatar'],
                    name=name
                ))

    def list_post(self):
        with open('assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    profile_pic=self.profile_picture,
                    avatar=data[username]['avatar'],
                    username=username,
                    post=data[username]['post'],
                    caption=data[username]['caption'],
                    likes=data[username]['likes'],
                    comments=data[username]['comments'],
                    posted_ago=data[username]['posted_ago']
                ))
