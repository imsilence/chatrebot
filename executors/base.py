#encoding: utf-8
from abc import ABCMeta, abstractmethod

class BaseExecutor(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self):
        return None