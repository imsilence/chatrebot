#encoding: utf-8

import time
import logging
from collections import namedtuple
from threading import Thread

logger = logging.getLogger(__name__)


class Scheduler(Thread):
    def __init__(self, tasks, mq, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.__tasks = tasks
        self.__mq = mq


    def __judge(self, now, time_tuple):
        _star_count = time_tuple.count('*')
        return now == now[:3 + _star_count] + tuple(time_tuple[_star_count:])


    def run(self):
        _sleep = 1
        _mq = self.__mq
        _tasks = self.__tasks
        _judge = self.__judge

        while True:
            _now = time.localtime()[:6]
            for _task in _tasks:
                _is_run = _judge(_now, _task.get("time"))
                logger.debug("judge task: %s, result: %s", _task, _is_run)
                if _is_run:
                    logger.info("schedule task: %s", _task)
                    _mq.put(_task)


            time.sleep(_sleep)

