import atexit

import picamera
from time import sleep
import io
from subprocess import call
import pygame
from pygame.locals import *
import os
from time import sleep
import screens
import gui.camera_sprite

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
displaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen = screens.TestScreen()

# Main loop ----------------------------------------------------------------

while True:

    # Refresh display
    gui.camera_sprite.has_updated = False
    screen.update()
    screen.draw(displaySurface)

    pygame.display.update()

    sleep(1/20.0)
