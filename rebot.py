#encoding: utf-8

import logging
import traceback
import threading
import os
import time

import itchat
from itchat.content import TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM
import wechatsogou

import gconf
from conf import tasks

from utils.mqueue import MQueue
from utils.cache import Cache
from utils.md5 import MD5
from handler import MsgHandler
from scheduler import TaskScheduler

from executors.text import TextExecutor
from executors.article import ArticleExecutor
from executors.joke import JokeExecutor

logger = logging.getLogger(__name__)

cache = Cache()
chat = itchat.new_instance()

@chat.msg_register([TEXT], isFriendChat=True)
def firendChat(msg):
    if msg.get("User").get("NickName") == gconf.ADMIN:
        logger.info(msg.get("Text"))


@chat.msg_register([TEXT], isGroupChat=True)
def groupChat(msg):
    #print("group:", msg)
    #return msg.get("Text")
    pass


@chat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM], isMpChat=True)
def mpChat(msg):
    print("mp:", msg)
    #return msg.get("Text")
    pass



@chat.msg_register([SHARING], isMpChat=True)
def sharingMsg(msg):
    try:
        item = {}
        item["name"] = msg.get("User").get("NickName")
        item["url"] = msg.get("Url")
        item["title"] = msg.get("Text")
        item["time"] = time.time() #msg.get("CreateTime")

        key = "{prefix}:{suffix}".format(prefix=gconf.REDIS_KEY_ARTICLE_PREFIX, suffix=MD5.enctype(item["name"]))
        cache.set(key, item)
        logger.info("cache sharing: %s", item)
    except BaseException as e:
        logger.exception(e)
        logger.error(traceback.format_exc())


def main():
    try:
        mq = MQueue("msg")
        chat.auto_login(hotReload=True, statusStorageDir=os.path.join(gconf.BASE_DIR, "temp", "chat.pkl"), enableCmdQR=2)

        handler = MsgHandler(chat, mq)
        handler.start()

        scheduler = TaskScheduler(mq)

        #scheduler.register("test_text", ("*", "*", 0), TextExecutor("Silence", "测试"))
        #scheduler.register("test_article", ("*", "*", 0), ArticleExecutor("Silence", "CSDN云计算", cache))
        #scheduler.register("lunch", (11, 45, 0), TextExecutor("Silence", "吃饭啦"))
        for text in tasks.TEXTS:
            scheduler.register(text.get("name"), text.get("time"), TextExecutor(**text))

        for article in tasks.ARTICLES:
            scheduler.register(article.get("name"), article.get("time"), ArticleExecutor(**article, cache=cache))

        for joke in tasks.JOKES:
            scheduler.register(joke.get("name"), joke.get("time"), JokeExecutor(**joke))



        scheduler.start()

        chat.run()
    except KeyboardInterrupt as e:
        logger.info("logout")
    except BaseException as e:
        logger.exception(e)
        logger.error(traceback.format_exc())
    finally:
        #chat.logout()
        pass

def write_pid():
    logger.info("running[%s]...", os.getpid())
    pid = os.path.join(gconf.BASE_DIR, "rebot.pid")
    with open(pid, "wt") as fhandler:
        fhandler.write(str(os.getpid()))

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s:%(message)s",
        filename=os.path.join(gconf.BASE_DIR, "logs", "rebot.log"),
        filemode="a"
    )
    write_pid()
    main()
