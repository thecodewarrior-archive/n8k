from pygame import *
from vec import vec
from typing import Union


iconPath = 'icons'  # Subdirectory containing UI bitmaps (PNG format)
icons = {}


class Icon:
    def __init__(self, name: str):
        self.name = name
        try:
            self.bitmap = image.load(iconPath + '/' + name + '.png')
        except:
            self.bitmap = Surface((32, 32))
            self.bitmap.fill((0, 0, 0))
            self.bitmap.fill((255, 0, 255), Rect(16, 0, 16, 16))
            self.bitmap.fill((255, 0, 255), Rect(0, 16, 16, 16))

    @staticmethod
    def create(name: str) -> 'Icon':
        if name in icons:
            return icons[name]
        icons[name] = Icon(name)
        return icons[name]


class Positioned:
    def __init__(self):
        self.rect = Rect((0, 0, 0, 0))

    # ints

    @property
    def top(self) -> int: return self.rect.top

    @property
    def bottom(self) -> int: return self.rect.bottom

    @property
    def left(self) -> int: return self.rect.left

    @property
    def right(self) -> int: return self.rect.right

    @property
    def centerx(self) -> int: return self.rect.centerx

    @property
    def centery(self) -> int: return self.rect.centery

    # vecs

    @property
    def topleft(self) -> vec: return vec.from_tuple(self.rect.topleft)

    @property
    def topright(self) -> vec: return vec.from_tuple(self.rect.topright)

    @property
    def bottomleft(self) -> vec: return vec.from_tuple(self.rect.bottomleft)

    @property
    def bottomright(self) -> vec: return vec.from_tuple(self.rect.bottomright)

    @property
    def center(self) -> vec: return vec.from_tuple(self.rect.center)

    # int setters

    @top.setter
    def top(self, value: int): self.rect.top = value

    @bottom.setter
    def bottom(self, value: int): self.rect.bottom = value

    @left.setter
    def left(self, value: int): self.rect.left = value

    @right.setter
    def right(self, value: int): self.rect.right = value

    @centerx.setter
    def centerx(self, value: int): self.rect.centerx = value

    @centery.setter
    def centery(self, value: int): self.rect.centery = value

    # vec setters

    @topleft.setter
    def topleft(self, value: vec): self.rect.topleft = (int(value.x), int(value.y))

    @topright.setter
    def topright(self, value: vec): self.rect.topright = (int(value.x), int(value.y))

    @bottomleft.setter
    def bottomleft(self, value: vec): self.rect.bottomleft = (int(value.x), int(value.y))

    @bottomright.setter
    def bottomright(self, value: vec): self.rect.bottomright = (int(value.x), int(value.y))

    @center.setter
    def center(self, value: vec): self.rect.center = (int(value.x), int(value.y))


class PGroup(sprite.OrderedUpdates, Positioned):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append

        for s in self.sprites():
            r = spritedict[s]
            img = s.image
            if s.rect.size == img.get_rect().size:
                img = transform.scale(img, s.rect.size)
            newrect = surface_blit(img, s.rect)
            if r:
                if newrect.colliderect(r):
                    dirty_append(newrect.union(r))
                else:
                    dirty_append(newrect)
                    dirty_append(r)
            else:
                dirty_append(newrect)
            spritedict[s] = newrect

        return dirty

    def sprite_under_point(self, pos: vec) -> Union[sprite.Sprite, None]:
        for e in reversed(self.sprites()):
            s = None
            if e is PGroup:
                s = e.sprite_under_point(pos)
            elif pos.inRect(e.rect):
                s = e
            if s is not None:
                return s
        return None
