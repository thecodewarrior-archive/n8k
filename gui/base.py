import pygame


iconPath = 'icons'  # Subdirectory containing UI bitmaps (PNG format)
icons = {}


class Icon:
    def __init__(self, name: str):
        self.name = name
        try:
            self.bitmap = pygame.image.load(iconPath + '/' + name + '.png')
        except:
            pass

    @staticmethod
    def create(name: str) -> 'Icon':
        if name in icons:
            return icons[name]
        icons[name] = Icon(name)
        return icons[name]
