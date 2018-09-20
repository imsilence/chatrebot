#encoding: utf-8

import os

BASE_DIR = os.path.normpath(os.path.dirname(__file__))

ADMIN = "Silence"

REDIS_CACHE = {
    "host" : "127.0.0.1",
    "port" : 6379,
    "db" : 0,
    "password" : None,
    "decode_responses" : True
}

REDIS_KEY_ARTICLE_PREFIX = "rebot:weixin:mp:last:article"


TULING_USERID = 'kk'
TULING_APIKEY = 'f5e166b44aae4be5912dfcbd6d3bb72b'