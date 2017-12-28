import pygame


class Screen:
    def __init__(self):
        self.group = pygame.sprite.RenderPlain()

    def update(self):
        self.group.update()

    def draw(self, surface: pygame.Surface):
        self.group.draw(surface)
