FROM ubuntu:15.10

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/ubuntu/ wily main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ wily-security main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ wily-updates main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ wily-proposed main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ wily-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ wily main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ wily-security main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ wily-updates main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ wily-proposed main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ wily-backports main restricted universe multiverse"\
>> sources.list &&\
apt-get update &&\
apt-get --yes --force-yes install git cmake ninja-build clang python uuid-dev libicu-dev icu-devtools libbsd-dev libedit-dev libxml2-dev libsqlite3-dev swig libpython-dev libncurses5-dev pkg-config &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
cd /home &&\
git clone https://github.com/apple/swift.git &&\
cd swift &&\
./utils/update-checkout --clone &&\
utils/build-script -t)

CMD ["bin/bash"]