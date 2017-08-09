FROM registry.aliyuncs.com/ericlung/ubuntu-python3

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (apt-get update &&\
apt-get --yes install nginx && \
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (pip install mkdocs mkdocs-material)

EXPOSE 8000



