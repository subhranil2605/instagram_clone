from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty


class CircularAvatarImage(MDRelativeLayout):
    avatar = StringProperty()
    name = StringProperty()
