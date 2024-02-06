import numpy as np
import cv2
from PIL import Image

def processing_image(img):
    grey=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
    resized=cv2.resize(grey,None,fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
    processed_image=cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )
    return processed_image