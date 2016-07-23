import multiprocessing

bind = "unix:/var/run/gunicorn/linknote.socket"
pidfile = "/var/run/gunicorn/linknote.pid"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '/var/log/gunicorn/gunicorn.linknote.access.log'
errorlog = '/var/log/gunicorn/gunicorn.linknote.error.log'
timeout = 300