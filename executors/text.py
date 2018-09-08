#encoding: utf-8
from datetime import datetime

from .base import BaseExecutor

class TextExecutor(BaseExecutor):

    def __init__(self, to, msg, tpl='[{time}]: {msg}',*args, **kwargs):
        self.to = to if isinstance(to, (tuple, list)) else [to]
        self.msg = msg
        self.tpl = tpl

    def execute(self):
        return True


    def get_to(self):
        return self.to


    def get_msg(self):
        return self.tpl.format(time=datetime.now().strftime("%Y-%m-%d %H:%M"), msg=self.msg)