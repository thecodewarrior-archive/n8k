import gui
from pygame import *


class TestScreen(gui.Screen):
    def __init__(self):
        super().__init__()

        cam = gui.CameraSprite()
        cam.rect.width = 320
        cam.rect.height = 240

        done = gui.Button("done", 320-10, "I'm Done!")
        done.rect.left = 5
        done.rect.bottom = self.rect.bottom - 5
        self.group.add(cam, done)
