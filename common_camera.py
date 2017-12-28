import picamera
import atexit

camera = picamera.PiCamera()

atexit.register(camera.close)
camera.resolution = (320, 240)
camera.crop = (0.0, 0.0, 1.0, 1.0)
