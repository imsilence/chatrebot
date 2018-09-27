#encoding: utf-8

from .subject import SUBJECT_SEC, SUBJECT_PYTHON, SUBJECT_JAVA


PROD_TASKS = [
    {
        "name" : "提醒起床",
        "type" : "text",
        "time" : (7, 30, 0),
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
        "kwargs" : {
            "msg" : "懒虫, 快起床啦!",
            "tpl" : "{msg}",
        }
    },
    {
        "name" : "午饭时刻",
        "type" : "text",
        "time" : (11, 45, 0),
        "to" : ["阳光可爱的帅气屌丝男士"],
        "kwargs" : {
            "msg" : "亲, 吃饭啦",
            "tpl" : "{msg}",
        }
    },
    {
        "name" : "浪荡时刻",
        "type" : "text",
        "time" : (17, 15, 0),
        "to" : ["阳光可爱的帅气屌丝男士"],
        "kwargs" : {
            "msg" : "亲, 出来浪荡啦",
            "tpl" : "{msg}",
        }
    },
    {
        "name" : "提醒睡眠",
        "type" : "text",
        "time" : (23, 00, 0),
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
        "kwargs" : {
            "msg" : "亲, 还没休息啊？ 明天早上可不要做赖床的懒猪猪哦!",
            "tpl" : "{msg}",
        }
    },
    {
        "time" : ("*", 0, 0),
        "type" : "article",
        "name" : "每小时推荐文章",
        "to" : ["Silence", "每小时文章"],
        "kwargs" : {
            "subjects" : SUBJECT_SEC + SUBJECT_JAVA + SUBJECT_PYTHON,
            "interval" : 60 * 60,
            "time_format" : "%Y-%m-%d %H:%M",
        }
    },
    {
        "time" : (9, 0, 0),
        "type" : "article",
        "name" : "安全推荐文章",
        "to" : ["阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "安全爱好者"],
        "kwargs" : {
            "subjects" : SUBJECT_SEC,
        }
    },
    {
        "time" : (9, 0, 0),
        "type" : "article",
        "name" : "Python推荐文章",
        "to" : ["Python爱好者", "Python 第18期"],
        "kwargs" : {
            "subjects" : SUBJECT_PYTHON,
        }
    },
    {
        "time" : (9, 0, 0),
        "type" : "article",
        "name" : "JAVA推荐文章",
        "to" : ["Java爱好者"],
        "kwargs" : {
            "subjects" : SUBJECT_JAVA,
        }
    },
    {
        "time" : (8, 30, 0),
        "type" : "joke",
        "name" : "每日笑话01",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
    {
        "time" : (12, 30, 0),
        "type" : "joke",
        "name" : "每日笑话02",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
    {
        "time" : (18, 30, 0),
        "type" : "joke",
        "name" : "每日笑话03",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
    {
        "time" : (21, 30, 0),
        "type" : "joke",
        "name" : "每日笑话04",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
]



TEST_TASKS = [
    {
        "name" : "测试文本",
        "type" : "text",
        "time" : ("*", "*", 0),
        "to" : ["Silence", "测试组"],
        "kwargs" : {
            "msg" : "测试",
            "tpl" : "{time}\n{msg}",
        }
    },
    {
        "name" : "测试文本",
        "type" : "text",
        "time" : ("*", 25, 0),
        "to" : ["Silence", "测试组"],
        "kwargs" : {
            "msg" : "测试(分钟)",
            "tpl" : "{time}\n{msg}",
        }
    },
    {
        "name" : "测试文本",
        "type" : "text",
        "time" : (22, 25, 0),
        "to" : ["Silence", "测试组"],
        "kwargs" : {
            "msg" : "测试(小时,分钟)",
            "tpl" : "{time}\n{msg}",
        }
    },
    {
        "name" : "测试笑话",
        "type" : "joke",
        "time" : ("*", "*", 0),
        "to" : ["Silence", "测试组"],
    },
    {
        "name" : "测试文章",
        "type" : "article",
        "time" : ("*", "*", 0),
        "to" : ["Silence", "测试组"],
        "kwargs" : {
            "subjects" : SUBJECT_SEC + SUBJECT_JAVA + SUBJECT_PYTHON,
            "topn" : 3,
            "interval" : 60 * 60,
            "time_format" : "%Y-%m-%d %H:%M:%S"
        }
    },

]


#TASKS = PROD_TASKS + TEST_TASKS
TASKS = PROD_TASKS
#TEST_TASKS