FROM postgres:12.3

MAINTAINER zpbird

RUN apt-get install -y apt-transport-https ca-certificates --no-install-recommends 

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" >/etc/apt/sources.list && \
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >>/etc/apt/sources.list && \
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >>/etc/apt/sources.list && \
echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >>/etc/apt/sources.list && \
apt-get update && \
apt-get install -y iproute2 supervisor htop glances --no-install-recommends && \
rm -rf /var/lib/apt/lists/*

COPY ./supervisor/ /etc/supervisor/
COPY ./other/localtime /etc/localtime

EXPOSE 7011

CMD ["/usr/bin/supervisord"]

