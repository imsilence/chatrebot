#encoding: utf-8

import hashlib

class MD5(object):

    @staticmethod
    def enctype(txt):
        if not isinstance(txt, bytes):
            txt = str(txt).encode()

        return hashlib.md5(txt).hexdigest()
