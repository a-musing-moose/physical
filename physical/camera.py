# -*- coding: utf-8 -*-
import io
import time
import picamera


RESOLUTION = (800, 600)


def capture_image():
    data = io.BytesIO()
    with picamera.PiCamera(resolution=RESOLUTION, framerate=10) as camera:
        time.sleep(1)  # Camera warm-up time
        camera.annotate_text = 'Hi MelbDjango!'
        camera.capture(data, 'jpeg')
    data.seek(0)
    return data
