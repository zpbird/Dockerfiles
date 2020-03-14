FROM python:3.7.6-buster

MAINTAINER zpbird

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo "deb https://mirrors.aliyun.com/debian/ buster main non-free contrib" >/etc/apt/sources.list && \
echo "deb https://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >>/etc/apt/sources.list && \
echo "deb https://mirrors.aliyun.com/debian-security buster/updates main" >>/etc/apt/sources.list && \
echo "deb https://mirrors.aliyun.com/debian buster-backports main non-free contrib" >>/etc/apt/sources.list && \
apt-get update && \
apt-get install -y supervisor htop --no-install-recommends && \
rm -rf /var/lib/apt/lists/* && \
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir \
gunicorn==20.0.4 \
gevent==1.4.0 \
Flask==1.1.1 \
Flask-SQLAlchemy==2.4.1 \
Flask-Migrate==2.5.2 \
Flask-script==2.0.6 \
Flask-RESTful==0.3.8 \
Flask-WTF==0.14.3 \
Flask-Login==0.5.0 \
Flask-OpenID==1.2.5 \
Flask-Session==0.3.1 \
Flask-Mail==0.9.1 \
Flask-Moment==0.9.0 \
Flask-Excel==0.0.7 \
Flask-Admin==1.5.5 \
Flask-SSE==0.2.1 \
Flask-CAS==1.0.0 \
Flask-SocketIO==4.2.1 \
celery==4.4.1 \
walrus==0.8.0

RUN mkdir /app

COPY ./supervisor/ /etc/supervisor/
COPY ./gunicorn/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py
COPY ./other/localtime /etc/localtime
COPY ./app_demo/ /app/

EXPOSE 8000 5000 7012

CMD ["/usr/bin/supervisord"]

