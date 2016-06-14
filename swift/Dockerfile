FROM ubuntu:16.04

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
>> sources.list &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

# Install related packages
RUN (apt-get update &&\
apt-get install -y build-essential clang wget libedit-dev python2.7 python2.7-dev rsync libxml2 git libssl-dev uuid-dev &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (SWIFT_ARCHIVE_NAME=swift-3.0-PREVIEW-1 &&\
SWIFT_URL=https://github.com/apple/swift/archive/$SWIFT_ARCHIVE_NAME.tar.gz &&\
wget $SWIFT_URL &&\
tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz --directory / --strip-components=1 &&\
rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/*)

# Set Swift Path
ENV PATH /usr/bin:$PATH

# Print Installed Swift Version
RUN swift --version