# 使用 #

1. 安装环境
```
    yum install redis
    yum install xdg-utils
    pip install -r requirements.txt
```

2. 配置

    修改订阅任务 conf/task.py
```
    TEXTS数组为文本任务, ARTICLES数组为订阅号文章任务

    公共参数:
        time: 执行时间, 元组类型, 示例:
            每天执行一次(9点): (9, 0, 0)
            每小时执行一次(9:10, 10:10, 11:10, ...): ("*", 10, 0)

        name: 任务名称, 不能重复
        to: 接受用户和群组列表

    文本任务:
        msg: 发送消息
        tpl: 模板, 默认: "[{time}]: {msg}", 字符串占位符只能包含time和msg

    文章任务:
        "subjects" : 订阅号文章
        "interval" : 最新发布的文章(interval秒)
        "topn": 发送文章最多数量
```
3. 登陆
```
    a. python rebot.py
    b. 手机扫描二维码登录
    c. 按ctrl+c退出
```
4. 启动
```
    nohup python rebot.py >/dev/null 2>&1 &
```
5. 查看日志
    logs/rebot.log
