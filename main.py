import os

import pygame
from vec import vec
import gui.camera_sprite
import screens

# Init framebuffer/touchscreen environment variables
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# Get user & group IDs for file & folder creation
# (Want these to be 'pi' or other user, not root)
s = os.getenv("SUDO_UID")
uid = int(s) if s else os.getuid()
s = os.getenv("SUDO_GID")
gid = int(s) if s else os.getgid()


# Init pygame and screen
pygame.init()
pygame.mouse.set_visible(False)
displaySurface = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)

screen = screens.TakePhoto()

# Main loop ----------------------------------------------------------------

clock = pygame.time.Clock()
print("Started!")
while True:

    for event in pygame.event.get():
        if event.type is pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            screen.mouse_down(vec.from_tuple(pos))
        if event.type is pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            screen.mouse_up(vec.from_tuple(pos))

    # Refresh display
    gui.camera_sprite.has_updated = False
    screen.update()
    screen.draw(displaySurface)

    pygame.display.update()

    clock.tick(20)

