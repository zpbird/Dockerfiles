FROM node:12.16.1-buster-slim

MAINTAINER zpbird

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" >/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian-security buster/updates main" >>/etc/apt/sources.list && \
echo "deb http://mirrors.aliyun.com/debian buster-backports main non-free contrib" >>/etc/apt/sources.list && \
apt-get update && \
apt-get install -y iproute2 supervisor htop --no-install-recommends && \
rm -rf /var/lib/apt/lists/* && \
mkdir /vue_src && \
npm config set registry https://registry.npm.taobao.org && \
npm install --silent --save-dev -g \
typescript eslint vue @vue/cli bable

COPY ./supervisor/ /etc/supervisor/
COPY ./other/localtime /etc/localtime

EXPOSE 7016

CMD ["/usr/bin/supervisord"]

