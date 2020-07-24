FROM		python:3.7-slim

RUN		    apt-get -y -qq update && \
		    apt-get -y -qq dist-upgrade && \
		    apt-get -u -qq autoremove

RUN         apt -y install nginx

# requirements.txt 복사
COPY	    ./requirements.txt /tmp/
RUN    		pip install -r /tmp/requirements.txt

# 소스코드 복사
COPY        . /srv/project-omok
WORKDIR     /srv/project-omok/app

# Nginx 기본 설정 삭제 & 설정 파일 복사
RUN         rm /etc/nginx/sites-enabled/default
RUN         cp /srv/project-omok/.config/omok.nginx /etc/nginx/sites-enabled/
RUN         cp /srv/project-omok/daphne.service /etc/systemd/system/
RUN         mkdir /var/log/gunicorn
RUN         mkdir /var/log/daphne

CMD         /bin/bash