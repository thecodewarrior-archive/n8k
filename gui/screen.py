import pygame
import gui


class Screen:
    def __init__(self):
        self.group = gui.PGroup()

    def update(self):
        self.group.update()

    def draw(self, surface: pygame.Surface):
        self.group.draw(surface)
