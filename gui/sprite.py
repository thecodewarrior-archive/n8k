import pygame.sprite

from gui.base import Icon


class Sprite(pygame.sprite.Sprite):
    def __init__(self, name: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.image = Icon.create(name).bitmap
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
