FROM tutum/debian:wheezy

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# aliyun sources\n\n\
deb http://mirrors.aliyun.com/debian/ wheezy main non-free contrib\n\
deb http://mirrors.aliyun.com/debian/ wheezy-proposed-updates main non-free contrib\n\
deb-src http://mirrors.aliyun.com/debian/ wheezy main non-free contrib\n\
deb-src http://mirrors.aliyun.com/debian/ wheezy-proposed-updates main non-free contrib\n"\
>> sources.list &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (apt-get update &&\
apt-get --yes install vim apache2 apache2-utils libapache2-mod-php5 php5-mysql &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (sed -i '2 s/^/\/etc\/init.d\/apache2 start\n/' /run.sh)

VOLUME ["/home"]
VOLUME ["/var/www"]

EXPOSE 80
EXPOSE 8888