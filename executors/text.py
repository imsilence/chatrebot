#encoding: utf-8
from datetime import datetime

from .base import BaseExecutor

class Executor(BaseExecutor):

    def __init__(self, msg, tpl='[{time}]: {msg}', *args, **kwargs):
        self.__msg = msg
        self.__tpl = tpl

    def __call__(self):
        yield self.__tpl.format(time=datetime.now().strftime("%Y-%m-%d %H:%M"), msg=self.__msg)