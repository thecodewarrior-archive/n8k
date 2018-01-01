import gui
import common_camera
from pygame import *
from vec import *


class TakePhoto(gui.Screen):
    def __init__(self):
        super().__init__()

        m = 5

        self.open_roi = gui.IconButton("open_controls", "open_roi_controls")
        self.open_roi.topright = self.topright + vec(-m, m)

        self.roi_controls = gui.PGroup()
        roi_up = gui.IconButton("up", "roi_up")
        roi_down = gui.IconButton("down", "roi_down")
        roi_left = gui.IconButton("left", "roi_left")
        roi_right = gui.IconButton("right", "roi_right")
        roi_in = gui.IconButton("in", "roi_in")
        roi_out = gui.IconButton("out", "roi_out")
        roi_close = gui.IconButton("close_controls", "open_roi_controls")

        roi_up.top = roi_in.top = self.top + 10  # top row
        roi_left.top = roi_close.top = roi_right.top = roi_in.bottom + m  # second row
        roi_down.top = roi_out.top = roi_right.bottom + m  # third row

        roi_in.right = roi_right.right = roi_out.right = self.right - 10  # rightmost column
        roi_up.right = roi_close.right = roi_down.right = roi_in.left - m  # second column
        roi_left.right = roi_close.left - m  # third column

        self.roi_controls.add(roi_up, roi_down, roi_left, roi_right, roi_in, roi_out, roi_close)

        common_camera.preview()
        cam = gui.CameraSprite()
        scale = min(self.rect.width / common_camera.resolution.x, self.rect.height / common_camera.resolution.y)
        cam.rect.width = int(common_camera.resolution[0] * scale)
        cam.rect.height = int(common_camera.resolution[1] * scale)
        cam.rect.center = self.rect.center

        done = gui.TextButton("done", 320-10, "I'm Done!")
        done.rect.left = 5
        done.rect.bottom = self.rect.bottom - 5
        done.onclick(
            lambda:
            print("I'm done here")
        )
        self.group.add(cam, done, self.open_roi)

    def button_click(self, name: str, button: gui.Button):
        print(name)
        if name == "open_controls":
            self.group.remove(self.open_roi)
            self.group.add(self.roi_controls)
        if name == "close_controls":
            self.group.remove(self.roi_controls)
            self.group.add(self.open_roi)
            common_camera.roi_reset()
        if name == "in":
            common_camera.roi_zoom_in()
        if name == "out":
            common_camera.roi_zoom_out()
        if name == "up":
            common_camera.roi_move(vec(0, -1))
        if name == "down":
            common_camera.roi_move(vec(0, 1))
        if name == "left":
            common_camera.roi_move(vec(-1, 0))
        if name == "right":
            common_camera.roi_move(vec(1, 0))

