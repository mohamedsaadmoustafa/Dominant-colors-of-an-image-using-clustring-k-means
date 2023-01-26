import numpy as np
import sys
import cv2

def GetImage(file):
    "Return image as numpyarray"
    print("Get Image", file=sys.stderr) # numpy array
    image = np.fromstring(file, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    assert( type(image) == np.ndarray )
    return image # numpy array

