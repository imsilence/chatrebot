#encoding: utf-8

from threading import Thread
import logging
import time

logger = logging.getLogger(__name__)

class MsgHandler(Thread):

    def __init__(self, chat, mq, *args, **kwargs):
        super(MsgHandler, self).__init__(*args, **kwargs)
        self.daemon = True
        self.chat = chat
        self.mq = mq

    def run(self):
        chat = self.chat
        mq = self.mq

        update_time = 0
        update_interval = 4 * 60 * 60
        friends = {}
        chatrooms = {}

        while True:
            item = mq.get()

            if not item:
                continue

            now = time.time()
            if update_time + update_interval <= now:
                friends = self.get_friends()
                chatrooms = self.get_chatrooms()
                update_time = now

            to = item.get("to")

            if not isinstance(to, (tuple, list)):
                to = [to]

            for touser in to:
                uid = friends.get(touser, chatrooms.get(touser))
                if uid:
                    chat.send(item.get("msg"), uid)
            logger.info("handler msg: %s, to:%s", item.get("msg"), item.get("to"))


    def get_friends(self):
        friends = {}
        for friend in self.chat.get_friends(update=True):
            name = friend.get('RemarkName', '')
            name = friend.get('NickName',  '') if name == '' else name
            name = name.encode(encoding="gbk", errors="ignore").decode(encoding="gbk")
            uid = friend.get('UserName', '')
            friends[name] = uid

        return friends


    def get_chatrooms(self):
        chatrooms = {}
        for chatroom in self.chat.get_chatrooms(update=True):
            name = chatroom.get('RemarkName', '')
            name = chatroom.get('NickName',  '') if name == '' else name
            name = name.encode(encoding="gbk", errors="ignore").decode(encoding="gbk")
            uid = chatroom.get('UserName', '')
            chatrooms[name] = uid

        return chatrooms