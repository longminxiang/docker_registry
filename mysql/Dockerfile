FROM mysql:5.7.10

MAINTAINER Eric Lung <longminxiang@163.com>

COPY ./opt /opt

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# aliyun sources\n\
deb http://mirrors.aliyun.com/debian jessie main contrib non-free\n\
deb-src http://mirrors.aliyun.com/debian jessie main contrib non-free\n\
deb http://mirrors.aliyun.com/debian jessie-updates main contrib non-free\n\
deb-src http://mirrors.aliyun.com/debian jessie-updates main contrib non-free\n\
deb http://mirrors.aliyun.com/debian-security jessie/updates main contrib non-free\n\
deb-src http://mirrors.aliyun.com/debian-security jessie/updates main contrib non-free"\
>> sources.list &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (apt-get update &&\
apt-get install -y cron vim &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (sed -i '2 s/^/sh \/opt\/setup.sh\n/' /entrypoint.sh)