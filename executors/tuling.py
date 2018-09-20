#encoding: utf-8

import os
import random
import logging
import traceback

import requests

import gconf
from .base import BaseExecutor

logger = logging.getLogger(__name__)

class TulingExecutor(BaseExecutor):

    def __init__(self, to, *args, **kwargs):
        self.to = to if isinstance(to, (tuple, list)) else [to]
        self.msg = None

    def execute(self, to, msg):

        json_content = {
            "reqType" : 0,
            "perception" : {
                "inputText": {
                    "text" : msg
                }
            },
            "userInfo" : {
                "apiKey" : gconf.TULING_APIKEY,
                "userId" : gconf.TULING_APIKEY,
            }
        }
        self.to = to
        self.msg = '不知道你说什么'

        try:
            response = requests.post("http://openapi.tuling123.com/openapi/api/v2", json=json_content, timeout=5)
            if not response.ok:
                return False

            json = response.json()
            for result in json.get("results", []):
                if "text" == result.get("resultType"):
                    self.msg = result.get("values", {}).get("text")
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