#encoding: utf-8

import time
from datetime import datetime, timedelta
import logging
from collections import namedtuple
from threading import Thread

logger = logging.getLogger(__name__)

class Task(object):

    def __init__(self, name, time, executor):
        self.name = name
        self.time = time
        self.executor = executor
        self.exec_time = None

    def __str__(self):
        return "[Task]{{name={name}, time={time}, exec_time={exec_time}}}".format(
                name=self.name,
                time=self.time,
                exec_time=self.exec_time
            )


class TaskScheduler(Thread):
    def __init__(self, mq, sleep=3, *args, **kwargs):
        super(TaskScheduler, self).__init__(*args, **kwargs)
        self.daemon = True
        self.mq = mq
        self.tasks = {}
        self.sleep = sleep

    def register(self, name, time, executor, *args, **kwargs):
        if name in self.tasks:
            raise Exception("task [{name}] already exists".format(name))
        self.tasks[name] = Task(name, time, executor)


    def judge(self, now, task):
        exec_time = task.exec_time
        next_exec_time = None
        star_count = task.time.count('*')

        timedeltas = [{"days" : 1}, {"hours" : 1}, {"minutes" : 1}, {"seconds" : 1}]

        if exec_time is None:
            exec_time = datetime(*(now.timetuple()[:3 + star_count] + tuple(task.time[star_count:])))
            if now < exec_time:
                exec_time -= timedelta(**timedeltas[star_count])
            task.exec_time = exec_time

        next_exec_time = exec_time + timedelta(**timedeltas[star_count])

        if now >= next_exec_time:
            task.exec_time = next_exec_time
            return True
        else:
            return False


    def run(self):
        mq = self.mq
        tasks = self.tasks
        sleep = self.sleep
        judge = self.judge

        while True:
            now = datetime.now()
            for name, task in tasks.items():
                if not judge(now, task):
                    continue

                logger.info("exec task: %s", task)
                executor = task.executor
                try:
                    if executor.execute():
                        mq.put({"to" : executor.get_to(), "msg" : executor.get_msg()})
                except BaseException as e:
                    logger.exception(e)
                    logger.error(traceback.format_exc())

            time.sleep(sleep)

