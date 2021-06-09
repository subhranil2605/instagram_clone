from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class PostCard(MDCard):
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
