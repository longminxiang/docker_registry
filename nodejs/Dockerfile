FROM ubuntu:16.04

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/ubuntu/ xenial main restricted\n\
deb-src http://mirrors.163.com/ubuntu/ xenial main restricted\n\
deb http://mirrors.163.com/ubuntu/ xenial-updates main restricted\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-updates main restricted\n\
deb http://mirrors.163.com/ubuntu/ xenial universe\n\
deb-src http://mirrors.163.com/ubuntu/ xenial universe\n\
deb http://mirrors.163.com/ubuntu/ xenial-updates universe\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-updates universe\n\
deb http://mirrors.163.com/ubuntu/ xenial multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-updates multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-updates multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ xenial-security main restricted\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-security main restricted\n\
deb http://mirrors.163.com/ubuntu/ xenial-security universe\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-security universe\n\
deb http://mirrors.163.com/ubuntu/ xenial-security multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ xenial-security multiverse"\
>> sources.list &&\
apt-get update &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (apt-get update &&\
apt-get --yes install vim git nodejs npm &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (npm install -g cnpm --registry=https://registry.npm.taobao.org && ln -s /usr/bin/nodejs /usr/bin/node)

RUN (cd / && echo "#!/bin/sh\nwhile true\ndo\nsleep 10000\ndone" >> run.sh && chmod 777 run.sh)

CMD ["/run.sh"]