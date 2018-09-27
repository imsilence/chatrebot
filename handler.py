#encoding: utf-8

from threading import Thread
import logging
import traceback
import time
import importlib

logger = logging.getLogger(__name__)

class Handler(Thread):

    def __init__(self, mq_task, mq_msg, cache, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.__mq_task = mq_task
        self.__mq_msg = mq_msg
        self.__cache = cache

    def run(self):
        _mq_task = self.__mq_task
        _mq_msg = self.__mq_msg
        _executors = {}
        _cache = self.__cache

        while True:
            _task = _mq_task.get()

            if not _task:
                continue

            _type = _task.get("type", "text")
            if _type not in _executors:
                _executors[_type] = None
                try:
                    _mod = importlib.import_module("executors.{0}".format(_type))
                    _executors[_type] = getattr(_mod, 'Executor', None)
                except ImportError as e:
                    logger.exception(e)
                    logger.error(traceback.format_exc())

            _executor = _executors.get(_type)
            if _executor:
                _to = _task.get("to", [])

                _kwargs = {'cache' : _cache, 'name' : _task.get('name', '')}
                _kwargs.update(_task.get("kwargs", {}))

                try:
                    for _msg in _executor(**_kwargs)():
                        logger.info("handler task: %s, msg:%s", _task, _msg)
                        _mq_msg.put({"msg" : _msg, "to" : _to})
                except BaseException as e:
                    logger.exception(e)
                    logger.error(traceback.format_exc())
