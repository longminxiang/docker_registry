FROM ubuntu:12.04

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse"\
>> sources.list &&\
apt-get update)

RUN (apt-get --yes --force-yes install python-dev python-pip &&\
cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple"\
>> pip.conf)

