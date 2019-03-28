FROM ubuntu:18.04

LABEL maintainer="EricLonger@163.com"

RUN cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ bionic main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ bionic-security main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ bionic-updates main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ bionic-proposed main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ bionic-backports main restricted universe multiverse"\
>> sources.list

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
apt-get --yes install python3 python3-pip libmysqlclient-dev vim tzdata &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
ln -s /usr/bin/python3 /usr/bin/python &&\
ln -s /usr/bin/pip3 /usr/bin/pip &&\
cd /root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple\n\
--trusted-host = pypi.douban.com" >> pip.conf &&\
pip install --upgrade pip

RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
echo Asia/Shanghai > /etc/timezone

ENV LANG C.UTF-8
