FROM postgres:12.3

MAINTAINER zpbird

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo "deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib" >/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian-security/ stretch/updates main" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >>/etc/apt/sources.list && \
apt-get update && \
apt-get install -y iproute2 supervisor htop glances --no-install-recommends && \
rm -rf /var/lib/apt/lists/*

COPY ./supervisor/ /etc/supervisor/
COPY ./other/localtime /etc/localtime

EXPOSE 7011

CMD ["/usr/bin/supervisord"]

