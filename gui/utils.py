from pygame import *


def create_filled_rounded_rect(size: (int, int), color: Color, radius: int) -> Surface:
    rect = Rect((0, 0), size)
    rectangle = Surface(rect.size, flags=SRCALPHA)

    ellipse_rect = Rect(0, 0, radius*2, radius*2)
    ellipse_rect.topleft = rect.topleft
    draw.ellipse(rectangle, color, ellipse_rect)
    ellipse_rect.topright = rect.topright
    draw.ellipse(rectangle, color, ellipse_rect)
    ellipse_rect.bottomright = rect.bottomright
    draw.ellipse(rectangle, color, ellipse_rect)
    ellipse_rect.bottomleft = rect.bottomleft
    draw.ellipse(rectangle, color, ellipse_rect)

    rectangle.fill(color, Rect(radius, 0, size[0] - radius*2, size[1]))
    rectangle.fill(color, Rect(0, radius, size[0], size[1] - radius*2))

    return rectangle


def erase_dot_grid(surface: Surface) -> Surface:
    for x in range(0, surface.get_width()):
        for y in range(0, surface.get_height()):
            if x % 2 == 1 or y % 2 == 1:
                color = surface.get_at((x, y))
                color.a //= 2
                surface.set_at((x, y), color)

    return surface

