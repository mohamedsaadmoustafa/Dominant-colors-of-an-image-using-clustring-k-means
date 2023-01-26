import numpy as np
from PIL import Image
import io
import base64


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