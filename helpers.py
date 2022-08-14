import numpy as np
from PIL import Image
import os , io , sys
import base64
import imutils
import cv2
import matplotlib.pyplot as plt

def GetImage(file):
    "Return image as numpyarray"
    print("Get Image", file=sys.stderr) # numpy array
    image = np.fromstring(file, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    assert( type(image) == np.ndarray )
    return image # numpy array


def PostImage( image ):
    ""
    assert( type(image) == np.ndarray )
    image = Image.fromarray(image.astype("uint8"))
    rawBytes = io.BytesIO()
    image.save(rawBytes, "JPEG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.getvalue()).decode('ascii')
    mime = "image/jpeg"
    return "data:%s;base64,%s" % (mime, img_base64)

def HexaColor(color: list):
    import binascii
    code = binascii.hexlify(bytearray(int(c) for c in color)).decode('ascii')
    return f"#{code}"

