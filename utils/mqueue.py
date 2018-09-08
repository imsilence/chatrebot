#encoding: utf-8

import json
from queue import Queue, Empty, Full

class MQueue(object):
    def __init__(self, name, serializer=json):
        self.name = name
        self.queue = Queue()
        self.serializer = serializer


    def get(self, timeout=3):
        try:
            item = self.queue.get(timeout=timeout)
            return self.serializer.loads(item) if self.serializer else item
        except Empty as e:
            return None


    def put(self, item, timeout=3):
        try:
            item = self.serializer.dumps(item) if self.serializer else item
            self.queue.put(item, timeout=timeout)
            return True
        except Full as e:
            return False


    def keys(self, pattern="*"):
        return self.rds.keys(pattern)