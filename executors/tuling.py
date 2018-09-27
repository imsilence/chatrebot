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

    def __init__(self, msg, *args, **kwargs):
        self.__msg = msg

    def __call__(self):
        _json_content = {
            "reqType" : 0,
            "perception" : {
                "inputText": {
                    "text" : self.__msg
                }
            },
            "userInfo" : {
                "apiKey" : gconf.TULING_APIKEY,
                "userId" : gconf.TULING_APIKEY,
            }
        }

        try:
            _response = requests.post("http://openapi.tuling123.com/openapi/api/v2", json=_json_content, timeout=5)
            if not _response.ok:
                return None

            _json = _response.json()
            for _result in _json.get("results", []):
                if "text" == _result.get("resultType"):
                    yield _result.get("values", {}).get("text")
                    break
        except BaseException as e:
            logger.exception(e)
            logger.error(traceback.format_exc())
            return None

