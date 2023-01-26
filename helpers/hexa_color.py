import binascii

def HexaColor(color: list):
    code = binascii.hexlify(bytearray(int(c) for c in color)).decode('ascii')
    return f"#{code}"

