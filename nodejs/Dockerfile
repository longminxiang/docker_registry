FROM debian:8.8

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/debian/ jessie main non-free contrib\n \
deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib\n \
deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib\n \
deb-src http://mirrors.163.com/debian/ jessie main non-free contrib\n \
deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib\n \
deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib\n \
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib\n \
deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib\n" \
>> sources.list &&\
apt-get update &&\
apt-get --yes install git curl &&\
curl -sL https://deb.nodesource.com/setup_8.x | bash - &&\
apt-get install --yes nodejs &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (npm config set registry https://registry.npm.taobao.org)
