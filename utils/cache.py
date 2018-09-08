#encoding: utf-8

import json

import redis

import gconf

class Cache(object):

    def __init__(self, serializer=json):
        self.rds = redis.StrictRedis(**gconf.REDIS_CACHE)
        self.serializer = serializer

    def get(self, key):
        item = self.rds.get(key)
        return self.serializer.loads(item) if item and self.serializer else item


    def set(self, key, item, ttl=None):
        item = self.serializer.dumps(item) if self.serializer else item
        self.rds.set(key, item, ttl)
        return True