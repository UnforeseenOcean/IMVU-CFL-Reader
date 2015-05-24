
__author__ = 'Toyz'

import struct
import pylzma

class InvalidCFLError(object):
    pass

CFLCOMPRESS_NONE = 0
CFLCOMPRESS_LZMA = 4

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def readInt(f):
        try:
            return struct.unpack('<I', f.read(4))[0]
        except struct.error:
            raise InvalidCFLError

    @staticmethod
    def compress(flag, plaintext):
        if flag == CFLCOMPRESS_NONE:
            return plaintext
        if flag == CFLCOMPRESS_LZMA:
            return pylzma.compress(plaintext)
        raise NotImplementedError('Unsupported flag %r' % (flag,))

    @staticmethod
    def decompress(flag, compressed):
        if flag == CFLCOMPRESS_NONE:
            return compressed
        if flag == CFLCOMPRESS_LZMA:
            try:
                return pylzma.decompress(compressed)
            except (TypeError, ValueError) as e:
                raise InvalidCFLError(e)
        else:
            raise InvalidCFLError('Unsupported flag %r' % (flag,))