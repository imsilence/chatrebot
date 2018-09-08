#encoding: utf-8

from .subject import SUBJECT_SEC, SUBJECT_PYTHON, SUBJECT_JAVA

TEXTS = [
    # {
    #     "name" : "文本测试",
    #     "time" : ("*", "*", 0),
    #     "to" : ["Silence"],
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
    #     "to" : ["Silence"],
    #     "subjects" : SUBJECT_SEC + SUBJECT_JAVA + SUBJECT_PYTHON,
    #     "topn" : 3,
    #     "interval" : 60 * 60
    # },
    {
        "time" : ("*", 0, 0),
        "name" : "每小时文章",
        "to" : ["Silence", "每小时文章"],
        "subjects" : SUBJECT_SEC + SUBJECT_JAVA + SUBJECT_PYTHON,
        "interval" : 60 * 60
    },
    {
        "time" : (9, 0, 0),
        "name" : "安全",
        "to" : ["阳光可爱的帅气屌丝男士", "绿源", "PPT小分队", "安全爱好者"],
        "subjects" : SUBJECT_SEC,
    },
    {
        "time" : (9, 0, 0),
        "name" : "Python",
        "to" : ["Python爱好者"],
        "subjects" : SUBJECT_PYTHON,
    },
    {
        "time" : (9, 0, 0),
        "name" : "JAVA",
        "to" : ["Java爱好者"],
        "subjects" : SUBJECT_JAVA,
    },
]