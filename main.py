import picamera
from time import sleep
import os
from subprocess import call

import pygame
from pygame.locals import *
import os
from time import sleep

os.chdir("/home/pi")

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
lcd = pygame.display.set_mode((320, 240))
# pygame.mouse.set_visible(False)
lcd.fill((255, 0, 0))
pygame.display.update()

print "filled screen"

font_big = pygame.font.Font(None, 50)
text_surface = font_big.render('Text!', True, (0, 0, 255))
rect = text_surface.get_rect(center=(160, 120))
lcd.blit(text_surface, rect)

print "drew text"

pygame.display.update()

print "starting loop"

while True:
    # Scan touchscreen events
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            print pos
        elif (event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            print pos
    sleep(0.1)

# INIT CAMERA
camera = picamera.PiCamera()

# camera.iso = 800
# # Wait for the automatic gain control to settle
# sleep(2)
# # Now fix the values
# camera.shutter_speed = camera.exposure_speed
# camera.exposure_mode = 'off'
# g = camera.awb_gains
# camera.awb_mode = 'off'
# camera.awb_gains = g

camera.resolution = (1920, 1080)
# camera.start_recording('video.h264')
# camera.wait_recording(60)
# camera.stop_recording()

