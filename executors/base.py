#encoding: utf-8
from abc import ABCMeta, abstractmethod

class BaseExecutor(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


    @abstractmethod
    def get_to(self):
        pass


    @abstractmethod
    def get_msg(self):
        pass
