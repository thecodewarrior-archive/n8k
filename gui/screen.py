import pygame
import gui
from vec import vec


class Screen(gui.Positioned):
    def __init__(self):
        super().__init__()
        self.group = gui.PGroup()
        self.rect = pygame.Rect(0, 0, 320, 240)
        self.mouse_clicked_on = None

    def update(self):
        self.group.update()

    def draw(self, surface: pygame.Surface):
        self.group.draw(surface)

    def mouse_down(self, pos: vec):
        self.mouse_clicked_on = self.group.sprite_under_point(pos)

    def mouse_up(self, pos: vec):
        s = self.group.sprite_under_point(pos)
        if self.mouse_clicked_on is s and isinstance(s, gui.Button):
            s.click()
            self.button_click(s.name, s)
        self.mouse_clicked_on = None

    def button_click(self, name: str, button: gui.Button):
        pass
