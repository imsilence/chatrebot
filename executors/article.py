#encoding: utf-8
import os
import logging
import traceback
import time
from datetime import datetime
from collections import namedtuple

import gconf
from utils.md5 import MD5
from .base import BaseExecutor

logger = logging.getLogger(__name__)


class ArticleExecutor(BaseExecutor):

    def __init__(self, name, to, subjects, cache, topn=15, interval=86400, *args, **kwargs):
        self.name = name
        self.to = to if isinstance(to, (tuple, list)) else [to]
        self.subjects = subjects if isinstance(subjects, (tuple, list)) else [subjects]
        self.cache = cache
        self.topn = topn
        self.articles = []
        self.interval = interval


    def execute(self):
        cache = self.cache
        interval = self.interval

        now = time.time()
        articles = []

        for subject in self.subjects:
            key = "{prefix}:{suffix}".format(prefix=gconf.REDIS_KEY_ARTICLE_PREFIX, suffix=MD5.enctype(subject))
            article = cache.get(key)
            if article and now - int(article.get("time")) < interval:
                articles.append(article)

        self.articles = articles[:self.topn]
        return len(articles)


    def get_to(self):
        return self.to


    def get_msg(self):
        msgs = ["[{0}]{1}推荐文章:\n".format(datetime.now().strftime("%Y-%m-%d"), self.name)]
        for idx, article in enumerate(self.articles):
            msgs.append("{idx}. [{name}]{title}\n{url}\n".format(idx=idx + 1, **article))
        return "\n".join(msgs)