# -*- coding: utf-8 -*-
import multiprocessing
import os
import gevent.monkey

gevent.monkey.patch_all()
if not os.path.exists('/var/log/gunicorn'):
    os.mkdir('/var/log/gunicorn')

# 生产环境不需要
debug = True

loglevel = 'debug'

# 后台运行
# daemon = True

# 修改源码后，不必重新启动进程，刷新页面即刻
reload = True

# 必须指定入口文件所在的目录
chdir = '/app'
bind = '0.0.0.0:7012'
worker_connections = 1200
pidfile = '/var/log/gunicorn/gunicorn.pid'
logfile = '/var/log/gunicorn/debug.log'
errorlog = '/var/log/gunicorn/error.log'
accesslog = '/var/log/gunicorn/access.log'
access_log_format = '%(h)s %(t)s %(U)s %(q)s'

# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
