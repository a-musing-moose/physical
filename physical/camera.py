# -*- coding: utf-8 -*-
import io
import time
import picamera


def capture_image():
    data = io.BytesIO()
    with picamera.PiCamera(resolution=(640, 480), framerate=10) as camera:
        time.sleep(1)  # Camera warm-up time
        camera.rotation = 270
        camera.annotate_text = 'Hi MelbDjango!'
        camera.capture(data, 'jpeg')
    data.seek(0)
    return data
