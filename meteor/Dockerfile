FROM longminxiang/ubuntu:16.04

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (apt-get update &&\
apt-get --yes install nodejs curl &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (curl https://install.meteor.com/ | sh)