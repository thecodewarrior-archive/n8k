import math
import io
import pygame
import numpy
import common_camera
from vec import vec


output = numpy.empty((1,))
camera_preview = pygame.Surface((1, 1))

has_updated = False


def raw_size() -> vec:
    return vec(32 * math.ceil(common_camera.resolution.x/32), 16 * math.ceil(common_camera.resolution.y/16))


def update_camsprite():
    global output, camera_preview, has_updated
    if has_updated:
        return

    common_camera.preview()
    size = raw_size()

    if output.shape[0] != int(size.y) or output.shape[1] != int(size.x):
        output = numpy.empty((int(size.y), int(size.x), 3), dtype=numpy.uint8)
        camera_preview = pygame.Surface((int(size.x), int(size.y)))

    common_camera.camera.capture(output, use_video_port=True, format='rgb')
    pygame.surfarray.blit_array(camera_preview, output.swapaxes(0, 1))

    has_updated = True


class CameraSprite(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(common_camera.resolution)
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()

    def update(self, *args):
        update_camsprite()
        self.dirty = 1
        self.image = camera_preview
