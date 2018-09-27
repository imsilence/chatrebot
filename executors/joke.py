#encoding: utf-8

import os
import random
import logging
import traceback

import requests

import gconf
from .base import BaseExecutor

logger = logging.getLogger(__name__)

class Executor(BaseExecutor):

    def __call__(self):
        _joke_content = None
        _joke_types = {"video" : "vid", "image" : "img", "gif" : "img"}
        try:
            _response = requests.get("https://www.apiopen.top/satinGodApi?type=1&page=1", timeout=5)
            if not _response.ok:
                return None

            _json = _response.json()
            if _json.get("code") != 200:
                return None

            _jokes = _json.get("data")
            for _ in range(10):
                _joke = random.choice(_jokes)
                _joke_type = _joke.get("type")
                _joke_content = _joke.get(_joke_type)
                if "text" == _joke_type:
                    yield _joke_content
                    break

                _response = requests.get(_joke_content)
                if not _response.ok:
                    continue

                _suffix = _joke_content.rpartition(".")[-1]
                _path = os.path.join(gconf.BASE_DIR, "temp", "{0}.{1}".format(random.randint(0, 10), _suffix))
                with open(_path, "wb") as _fhandler:
                    _fhandler.write(_response.content)

                yield "@{0}@{1}".format(_joke_types.get(_joke_type), _path)
                break

        except BaseException as e:
            logger.exception(e)
            logger.error(traceback.format_exc())
            return None