FROM nginx:1.16.1

MAINTAINER zpbird

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" >/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian-security buster/updates main" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian buster-backports main non-free contrib" >>/etc/apt/sources.list && \
apt-get update && \
apt-get install -y iproute2 supervisor htop glances --no-install-recommends && \
rm -rf /var/lib/apt/lists/*

COPY ./supervisor/ /etc/supervisor/
COPY ./other/localtime /etc/localtime
COPY ./html/ /usr/share/nginx/html/
COPY ./conf.d/ /etc/nginx/conf.d/
COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 5000 8000 7011

STOPSIGNAL SIGTERM

CMD ["/usr/bin/supervisord"]

