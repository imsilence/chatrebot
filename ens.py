#encoding: utf-8

from threading import Thread
import logging
import time

logger = logging.getLogger(__name__)

class ENS(Thread):

    def __init__(self, chat, mq, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.__chat = chat
        self.__mq = mq

    def run(self):
        _chat = self.__chat
        _mq = self.__mq

        _update_time = 0
        _update_interval = 4 * 60 * 60
        _friends = {}
        _chatrooms = {}

        while True:
            _item = _mq.get()

            if not _item:
                continue

            _now = time.time()
            if _update_time + _update_interval <= _now:
                _friends = self.__get_friends()
                _chatrooms = self.__get_chatrooms()
                _update_time = _now

            _to = _item.get("to")

            if not isinstance(_to, (tuple, list)):
                _to = [_to]


            for _touser in _to:
                _uid = _friends.get(_touser, _chatrooms.get(_touser, _touser))
                try:
                    _chat.send(_item.get("msg"), _uid)
                except BaseException as e:
                    logger.exception(e)
                    logger.error(traceback.format_exc())


    def __get_friends(self):
        _friends = {}
        for _friend in self.__chat.get_friends(update=True):
            _name = _friend.get("RemarkName", "")
            _name = _friend.get("NickName",  "") if _name == "" else _name
            _name = _name.encode(encoding="gbk", errors="ignore").decode(encoding="gbk")
            _uid = _friend.get("UserName", "")
            _friends[_name] = _uid

        return _friends


    def __get_chatrooms(self):
        _chatrooms = {}
        for _chatroom in self.__chat.get_chatrooms(update=True):
            _name = _chatroom.get("RemarkName", "")
            _name = _chatroom.get("NickName",  "") if _name == "" else _name
            _name = _name.encode(encoding="gbk", errors="ignore").decode(encoding="gbk")
            _uid = _chatroom.get("UserName", "")
            _chatrooms[_name] = _uid

        return _chatrooms