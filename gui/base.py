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


class PGroup(pygame.sprite.AbstractGroup):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        """draw all sprites onto the surface
        Group.draw(surface): return None
        Draws all of the member sprites onto the given surface.
        """
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            if spr.rect.size == spr.image.get_rect().size:
                self.spritedict[spr] = surface_blit(spr.image, spr.rect)
            else:
                scaled = pygame.transform.scale(spr.image, spr.rect.size)
                self.spritedict[spr] = surface_blit(scaled, spr.rect)

        self.lostsprites = []