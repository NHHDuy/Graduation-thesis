from src.compat import bytes, str, bytes_types, is_py2

import codecs
import binascii

def is_string(value):
    return isinstance(value, bytes_types)

def to_string(value):
    if is_string(value):
        return value
    elif isinstance(value, str):
        if not is_py2:
            value = value.encode()
        return value
    else:
        value = str(value)
        if not is_py2:
            value = value.encode()
        return bytes(value)

def to_hex(value):
    if not is_py2:
        return to_string(value).hex()
    return codecs.encode(to_string(value), "hex")

def from_hex(value):
    try:
        if not is_py2:
            return bytes.fromhex(value)
        return bytes(bytearray.fromhex(value))
    except Exception as error:
        if isinstance(error, binascii.Error):
            raise
        pass
    return value