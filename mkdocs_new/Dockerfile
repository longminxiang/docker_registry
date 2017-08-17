FROM registry.aliyuncs.com/ericlung/ubuntu-python3

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (apt-get update &&\
apt-get --yes install nginx && \
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (pip install mkdocs==0.16.3 mkdocs-material==1.8.1)

EXPOSE 8000



