#encoding: utf-8

import logging
import traceback
import threading
import os
import time

import itchat
from itchat.content import TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM

import gconf
from conf import tasks

from utils.mqueue import MQueue
from utils.cache import Cache
from utils.md5 import MD5
from ens import ENS
from handler import Handler
from scheduler import Scheduler

logger = logging.getLogger(__name__)

cache = Cache()
mq_task = MQueue("task")
mq_msg = MQueue("msg")

chat = itchat.new_instance()


@chat.msg_register([TEXT], isFriendChat=True)
def firendChat(msg):
    if msg.get("User").get("NickName") == gconf.ADMIN:
        logger.debug("Admin Chat: %s", msg.get("Text"))
        return "收到消息:{0}".format(msg.get("Text"))


@chat.msg_register([TEXT], isGroupChat=True)
def groupChat(msg):
    if msg.get("IsAt"):
        logger.debug("group Chat: %s", msg.get("Text"))
        mq_task.put({
            "name" : "群聊@",
            "type" : "tuling",
            "to" : msg.get("FromUserName"),
            "kwargs" : {
                "msg" : msg.get("Text")
            }
        })



@chat.msg_register([SHARING], isMpChat=True)
def mpChatSharing(msg):
    try:
        _item = {}
        _item["name"] = msg.get("User").get("NickName")
        _item["url"] = msg.get("Url")
        _item["title"] = msg.get("Text")
        _item["time"] = time.time() #msg.get("CreateTime")

        _key = "{prefix}:{suffix}".format(prefix=gconf.REDIS_KEY_ARTICLE_PREFIX, suffix=MD5.enctype(_item["name"]))
        cache.set(_key, _item)
        logger.info("cache sharing: %s", _item)
    except BaseException as e:
        logger.exception(e)
        logger.error(traceback.format_exc())


def main():
    try:
        chat.auto_login(hotReload=True, statusStorageDir=os.path.join(gconf.BASE_DIR, "temp", "chat.pkl"), enableCmdQR=2)

        for _ in range(10):
            ENS(chat, mq_msg).start()

        for _ in range(10):
            Handler(mq_task, mq_msg, cache).start()

        Scheduler(tasks.TASKS, mq_task).start()

        chat.run()
    except KeyboardInterrupt as e:
        logger.info("logout")
    except BaseException as e:
        logger.exception(e)
        logger.error(traceback.format_exc())
    finally:
        pass


def write_pid():
    _pid = os.getpid()
    logger.info("running[%s]...", _pid)
    _ppath = os.path.join(gconf.BASE_DIR, "rebot.pid")
    with open(_ppath, "wt") as _fhandler:
        _fhandler.write(str(_pid))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s:%(message)s",
        filename=os.path.join(gconf.BASE_DIR, "logs", "rebot.log"),
        filemode="w"
    )
    write_pid()
    main()
