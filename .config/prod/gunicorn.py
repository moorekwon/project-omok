daemon = False
chdir = '/srv/omok/app'
bind = 'unix:/run/omok.sock'
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
capture_output = True
