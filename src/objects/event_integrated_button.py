from pygame.sprite import AbstractGroup

from src.objects.animated_button import AnimatedButton


class EventIntegratedButton(AnimatedButton):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.change_frame(1, "images/default.png")
        self.change_frame(0, "images/default.png")

    def update(self, *args, **kwargs) -> None:
        super(EventIntegratedButton, self).update(*args, **kwargs)
        if self.is_hovering():
            self.set_custom_frame(1)
        else:
            self.set_custom_frame(0)

    def set_hover_image_path(self, path: str) -> None:
        self.change_frame(1, path)

    def set_default_image_path(self, path: str) -> None:
        self.change_frame(0, path)
