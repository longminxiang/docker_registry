FROM index.alauda.cn/library/ubuntu:16.04

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# aliyun sources\n\n\
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted\n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted\n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted\n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted\n\
deb http://mirrors.aliyun.com/ubuntu/ xenial universe\n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial universe\n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe\n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates universe\n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted\n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted\n\
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe\n\
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security universe\n"\
>> sources.list && apt-get update)

RUN (apt-get --yes install python3.5 python3-pip && \
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (ln /usr/bin/python3.5 /bin/python &&\
ln /usr/bin/pip3 /bin/pip &&\
cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple\n\
--trusted-host = pypi.douban.com"\
>> pip.conf)
