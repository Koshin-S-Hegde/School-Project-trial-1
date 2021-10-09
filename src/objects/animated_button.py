from src.objects.button import Button
from src.objects.animated_object import AnimatedObject


class AnimatedButton(Button, AnimatedObject):

    def __init__(self):
        super().__init__()
