import pygame.sprite
import gui


class Sprite(pygame.sprite.DirtySprite, gui.Positioned):
    def __init__(self, name: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.image = gui.Icon.create(name).bitmap
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
