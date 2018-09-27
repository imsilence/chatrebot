#encoding: utf-8
import os
import logging
import traceback
import time
from datetime import datetime
from collections import namedtuple

import gconf
from utils.md5 import MD5
from utils.url import URL
from .base import BaseExecutor

logger = logging.getLogger(__name__)


class Executor(BaseExecutor):

    def __init__(self, name, subjects, cache, topn=15, interval=86400, time_format="%Y-%m-%d", *args, **kwargs):
        self.__name = name
        self.__subjects = subjects if isinstance(subjects, (tuple, list)) else [subjects]
        self.__cache = cache
        self.__topn = topn
        self.__interval = interval
        self.__time_format = time_format


    def __call__(self):
        _name = self.__name
        _cache = self.__cache
        _interval = self.__interval
        _subjects = self.__subjects
        _time_format = self.__time_format

        _articles = []

        _now = time.time()
        for _subject in _subjects:
            _key = "{prefix}:{suffix}".format(prefix=gconf.REDIS_KEY_ARTICLE_PREFIX, suffix=MD5.enctype(_subject))
            _article = _cache.get(_key)
            if _article and _now - int(_article.get("time")) < _interval:
                _articles.append(_article)

        if _articles:
            _msgs = ["[{0}]{1}:\n".format(datetime.now().strftime(_time_format), _name)]
            for idx, _article in enumerate(_articles):
                _article["url"] = URL.short(_article.get("url")) # short url
                _msgs.append("{idx}. [{name}]{title}\n{url}\n".format(idx=idx + 1, **_article))
            yield "\n".join(_msgs)

