FROM centos:7

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (yum -y install wget)

RUN (cd /etc/yum.repos.d/ && wget -O CentOS-Base.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo)

RUN (yum clean all && yum -y makecache)
