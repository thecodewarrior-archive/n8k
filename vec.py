import pygame
from typing import NamedTuple, Union

class vec(NamedTuple('vec', [('x', float), ('y', float)])):

    def __neg__(self) -> 'vec':
        return vec(-self.x, -self.y)

    def __add__(self, other: 'vec') -> 'vec':
        return vec(self.x + other.x, self.y + other.y)

    def __concat__(self, other: 'vec') -> 'vec':
        # Not sure if this will be called, since we are a tuple, and thus a sequence
        return vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'vec') -> 'vec':
        return vec(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, int, 'vec']) -> 'vec':
        if isinstance(other, (float, int)):
            return vec(self.x * other, self.y * other)
        elif isinstance(other, vec):
            return vec(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: Union[float, int, 'vec']) -> 'vec':
        if isinstance(other, (float, int)):
            return vec(self.x / other, self.y / other)
        elif isinstance(other, vec):
            return vec(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other: Union[float, int, 'vec']) -> 'vec':
        if isinstance(other, (float, int)):
            return vec(self.x // other, self.y // other)
        elif isinstance(other, vec):
            return vec(self.x // other.x, self.y // other.y)

    def __mod__(self, other: Union[float, int, 'vec']) -> 'vec':
        if isinstance(other, (float, int)):
            return vec(self.x % other, self.y % other)
        elif isinstance(other, vec):
            return vec(self.x % other.x, self.y % other.y)

    def inRect(self, rect: pygame.Rect) -> bool:
        return 0 <= self.x - rect.x <= rect.width and 0 <= self.y - rect.y <= rect.height

    @staticmethod
    def from_tuple(tup: (float, float)) -> 'vec':
        return vec(tup[0], tup[1])

