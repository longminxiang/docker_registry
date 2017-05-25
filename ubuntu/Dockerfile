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
apt-get --yes install python python-pip python-dev vim &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple\n\
--trusted-host = pypi.douban.com"\
>> pip.conf &&\
sed -i '1 s/^/import sys\n\nreload(sys)\nsys.setdefaultencoding("utf8")\n\n/' /usr/lib/python2.7/sitecustomize.py)

RUN (pip install --upgrade pip)