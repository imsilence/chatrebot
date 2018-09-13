#encoding: utf-8

import logging
import traceback
import requests

logger = logging.getLogger(__name__)

class URL(object):

    @staticmethod
    def short(url):
        try:
            response = requests.post("http://dwz.cn/admin/create", json={"url" : url})
            if response.ok:
                json = response.json()
                if json.get("Code") == 0:
                    return json.get("ShortUrl")
        except BaseException as e:
            logger.exception(e)
            logger.error(traceback.format_exc())

        return url

if __name__ == '__main__':
    print(URL.short("http://www.baidu.com"))