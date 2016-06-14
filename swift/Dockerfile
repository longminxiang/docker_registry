FROM ubuntu:14.04

MAINTAINER Eric Lung <longminxiang@163.com>

# Change souces
RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# aliyun sources\n\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse"\
>> sources.list &&\
apt-get clean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

# Install related packages
RUN (apt-get update &&\
apt-get install -y build-essential wget clang libedit-dev \
python2.7 python2.7-dev libicu52 rsync libxml2 git libssl-dev uuid-dev &&\
apt-get clean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

# Install Swift keys
RUN (wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - &&\
gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift)

ENV SWIFT_VERSION 3.0-preview-1
ENV SWIFT_PLATFORM ubuntu14.04

# Install Swift Ubuntu 14.04 Snapshot
RUN (SWIFT_ARCHIVE_NAME=swift-$SWIFT_VERSION-$SWIFT_PLATFORM && \
SWIFT_URL=https://swift.org/builds/swift-$SWIFT_VERSION/$(echo "$SWIFT_PLATFORM" | tr -d .)/swift-$SWIFT_VERSION/$SWIFT_ARCHIVE_NAME.tar.gz && \
wget $SWIFT_URL && \
wget $SWIFT_URL.sig && \
gpg --verify $SWIFT_ARCHIVE_NAME.tar.gz.sig && \
tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz --directory / --strip-components=1 && \
rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/*)

# Set Swift Path
ENV PATH /usr/bin:$PATH

# Print Installed Swift Version
RUN swift --version