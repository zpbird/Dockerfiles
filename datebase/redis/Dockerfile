FROM redis:5.0.8-buster

MAINTAINER zpbird

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" >/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian-security buster/updates main" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian buster-backports main non-free contrib" >>/etc/apt/sources.list && \
apt-get update && \
apt-get install -y supervisor htop glances --no-install-recommends && \
rm -rf /var/lib/apt/lists/*

COPY ./supervisor/ /etc/supervisor/
COPY ./other/localtime /etc/localtime

EXPOSE 6379

CMD ["/usr/bin/supervisord"]

