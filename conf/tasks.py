#encoding: utf-8

from .subject import SUBJECT_SEC, SUBJECT_PYTHON, SUBJECT_JAVA

TEXTS = [
    # {
    #     "name" : "文本测试",
    #     "time" : ("*", "*", 0),
    #     "to" : ["Silence", "测试组"],
    #     "msg" : "测试",
    #     "tpl" : "{time}\n{msg}",
    # },
    {
        "name" : "午饭时刻",
        "time" : (11, 45, 0),
        "to" : ["阳光可爱的帅气屌丝男士"],
        "msg" : "亲, 吃饭啦",
        "tpl" : "{msg}",
    },
    {
        "name" : "浪荡时刻",
        "time" : (17, 15, 0),
        "to" : ["阳光可爱的帅气屌丝男士"],
        "msg" : "亲, 出来浪荡啦",
        "tpl" : "{msg}",
    },
]

ARTICLES = [
    # {
    #     "time" : ("*", "*", 0),
    #     "name" : "测试文章",
    #     "to" : ["Silence", "测试组"],
    #     "subjects" : SUBJECT_SEC + SUBJECT_JAVA + SUBJECT_PYTHON,
    #     "topn" : 3,
    #     "interval" : 60 * 60
    # },
    {
        "time" : ("*", 0, 0),
        "name" : "每小时推荐文章",
        "to" : ["Silence", "每小时文章"],
        "subjects" : SUBJECT_SEC + SUBJECT_JAVA + SUBJECT_PYTHON,
        "interval" : 60 * 60
    },
    {
        "time" : (9, 0, 0),
        "name" : "安全推荐文章",
        "to" : ["阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "安全爱好者"],
        "subjects" : SUBJECT_SEC,
    },
    {
        "time" : (9, 0, 0),
        "name" : "Python推荐文章",
        "to" : ["Python爱好者", "Python 第18期"],
        "subjects" : SUBJECT_PYTHON,
    },
    {
        "time" : (9, 0, 0),
        "name" : "JAVA推荐文章",
        "to" : ["Java爱好者"],
        "subjects" : SUBJECT_JAVA,
    },
]

JOKES = [
    # {
    #     "time" : ("*", "*", 0),
    #     "name" : "测试笑话",
    #     "to" : ["Silence", "测试组"],
    # },
    {
        "time" : (8, 30, 0),
        "name" : "每日笑话01",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
    {
        "time" : (12, 30, 0),
        "name" : "每日笑话02",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
    {
        "time" : (18, 30, 0),
        "name" : "每日笑话03",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
    {
        "time" : (21, 30, 0),
        "name" : "每日笑话04",
        "to" : ["执子之手与子偕老", "阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "男人帮", "新二货群", "有事没事聊聊天"],
    },
]