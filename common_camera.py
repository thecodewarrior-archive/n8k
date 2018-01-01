import math
import numpy
import picamera
import atexit
from vec import vec
from enum import Enum


class CameraMode(Enum):
    video = 1
    picture = 2
    preview = 3


CAMERA_RESOLUTION = vec(2592, 1944)
camera = picamera.PiCamera()
atexit.register(camera.close)
resolution = vec(0, 0)
crop_size = vec(1, 1)
current_mode = CameraMode.video


def clamp(v: float, minv: float, maxv: float) -> float:
    return max(minv, min(maxv, v))


def enter_picture_mode():
    global resolution, crop_size, current_mode
    resolution = vec(2592, 1944)
    crop_size = vec(1, 1)
    current_mode = CameraMode.picture
    update_video()


def enter_video_mode():
    global resolution, crop_size, current_mode
    resolution = vec(1920, 1080)
    crop_size = vec(0.7408, 0.5556)
    current_mode = CameraMode.video
    update_video()


def update_video():
    camera.resolution = resolution
    camera.crop = ((1-crop_size.x)/2, (1-crop_size.y)/2, crop_size.x, crop_size.y)


preview_zoom = 1
preview_center = vec(0.5, 0.5)
move_fraction = 1/4
preview_update = True


def roi_validate():
    global preview_zoom, preview_center, preview_update
    preview_update = True

    if preview_zoom <= 0:
        preview_zoom = 1
    roi_resolution = CAMERA_RESOLUTION / preview_zoom
    if roi_resolution.x < 320 or roi_resolution.y < 240:
        preview_zoom -= 1

    preview_center = vec(
        clamp(preview_center.x, 0.5/preview_zoom, 1-(0.5/preview_zoom)),
        clamp(preview_center.y, 0.5/preview_zoom, 1-(0.5/preview_zoom))
    )


def roi_zoom_in():
    global preview_zoom
    preview_zoom += 1
    roi_validate()


def roi_zoom_out():
    global preview_zoom
    preview_zoom -= 1
    roi_validate()


def roi_move(direction: vec):
    global preview_center
    preview_center += direction * (move_fraction/preview_zoom)
    roi_validate()


def roi_reset():
    global preview_zoom, preview_center
    preview_center = vec(0.5, 0.5)
    preview_zoom = 1
    roi_validate()


def preview():
    global resolution, preview_update, current_mode
    if current_mode is CameraMode.preview and not preview_update:
        return
    resolution = vec(320, 240)

    size = crop_size
    size /= preview_zoom
    pos = vec(1, 1)
    pos -= crop_size
    pos /= 2
    pos += preview_center*crop_size - size/2

    camera.resolution = resolution
    camera.zoom = (pos.x, pos.y, size.x, size.y)

    current_mode = CameraMode.preview
    preview_update = False


enter_picture_mode()
