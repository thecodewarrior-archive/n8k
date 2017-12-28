import io
import pygame
import yuv2rgb
import common_camera


def camera_pixels() -> int:
    return common_camera.camera.resolution.width * common_camera.camera.resolution.height


# Buffers for viewfinder data
rgb = bytearray(camera_pixels() * 3)
yuv = bytearray((camera_pixels() * 3) // 2)

camera_preview = pygame.Surface(common_camera.camera.resolution)
camera_preview.fill((255, 0, 255))

has_updated = False


def update_camsprite():
    global rgb, yuv, camera_preview, has_updated
    if has_updated:
        return

    if len(rgb) != camera_pixels() * 3:
        rgb = bytearray(camera_pixels() * 3)
        yuv = bytearray((camera_pixels() * 3) // 2)

    size = common_camera.camera.resolution

    stream = io.BytesIO()  # Capture into in-memory stream
    common_camera.camera.capture(stream, use_video_port=True, format='raw')
    stream.seek(0)
    stream.readinto(yuv)  # stream -> YUV buffer
    stream.close()
    yuv2rgb.convert(yuv, rgb, size.width, size.height)

    camera_preview = pygame.image.frombuffer(rgb[0: (size.width * size.height * 3)], size, 'RGB')

    has_updated = True


class CameraSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(common_camera.camera.resolution)
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()

    def update(self, *args):
        update_camsprite()
        self.image = camera_preview
        self.rect.size = camera_preview.get_rect().size
