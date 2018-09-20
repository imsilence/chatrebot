#encoding: utf-8

import os
import random
import logging
import traceback

import requests

import gconf
from .base import BaseExecutor

logger = logging.getLogger(__name__)

class JokeExecutor(BaseExecutor):

    def __init__(self, to, *args, **kwargs):
        self.to = to if isinstance(to, (tuple, list)) else [to]
        self.msg = None

    def execute(self):
        joke_content = None
        joke_types = {"video" : "vid", "image" : "img", "gif" : "img"}
        try:
            response = requests.get("https://www.apiopen.top/satinGodApi?type=1&page=1", timeout=5)
            if not response.ok:
                return False

            json = response.json()
            if json.get("code") != 200:
                return False

            jokes = json.get("data")
            for _ in range(10):
                joke = random.choice(jokes)
                joke_type = joke.get("type")
                joke_content = joke.get(joke_type)
                if "text" == joke_type:
                    self.msg = joke_content
                    break

                response = requests.get(joke_content)
                if not response.ok:
                    continue

                suffix = joke_content.rpartition(".")[-1]
                path = os.path.join(gconf.BASE_DIR, "temp", "{0}.{1}".format(random.randint(0, 10), suffix))
                with open(path, "wb") as fhandler:
                    fhandler.write(response.content)
                self.msg = "@{0}@{1}".format(joke_types.get(joke_type), path)
                break

            return self.msg
        except BaseException as e:
            logger.exception(e)
            logger.error(traceback.format_exc())
            return False


    def get_to(self):
        return self.to


    def get_msg(self):
        return self.msg
