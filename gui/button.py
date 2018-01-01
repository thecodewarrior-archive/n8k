import gui
from gui.utils import *
from pygame import *
from typing import Callable


class Button(gui.Sprite):
    def __init__(self, name: str):
        super().__init__(name, 0, 0)
        self._click_handlers = []

    def onclick(self, callback: Callable):
        self._click_handlers.append(callback)

    def click(self):
        for handler in self._click_handlers:
            handler()


class IconButton(Button):
    def __init__(self, name: str, icon: str):
        super().__init__(name)

        self.icon = gui.Icon.create(icon)
        self.rect = self.icon.bitmap.get_rect()

        self.update_surface()

    def update_surface(self):
        b = 48
        background_surface = erase_dot_grid(create_filled_rounded_rect(self.rect.size, Color(b, b, b, 255), 10))

        icon_rect = self.icon.bitmap.get_rect()
        icon_rect.center = background_surface.get_rect().center
        background_surface.blit(self.icon.bitmap, icon_rect)

        self.image = background_surface


class TextButton(Button):
    def __init__(self, name: str, width: int, text: str):
        super().__init__(name)

        self.rect = Rect(0, 0, width, 30)
        self.text = text
        self.font = font.SysFont("FreeSans", 24)
        self.textColor = Color("white")

        self.update_surface()

    def update_surface(self):
        b = 48
        background_surface = erase_dot_grid(create_filled_rounded_rect(self.rect.size, Color(b, b, b, 255), 10))
        text_surface = self.font.render(self.text, True, self.textColor)

        text_rect = text_surface.get_rect()
        text_rect.center = background_surface.get_rect().center
        background_surface.blit(text_surface, text_rect)

        self.image = background_surface
