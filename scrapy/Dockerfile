FROM index.alauda.cn/library/centos:7

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (yum -y update &&\
yum -y install epel-release &&\
yum clean all)

RUN (yum -y install python-pip python-devel gcc openssl-devel \
libffi-devel libxslt-devel libxml2-devel &&\
yum clean all)

RUN (cd root &&\
mkdir .pip &&\
cd .pip &&\
echo -e "\n[global]\n\
index-url = http://pypi.douban.com/simple\n\
--trusted-host = pypi.douban.com"\
>> pip.conf &&\
cd /usr/lib/python2.7/site-packages/ &&\
echo -e "import sys\n\
sys.setdefaultencoding('utf-8')"\
>> sitecustomize.py)

RUN (pip install --upgrade pip &&\
pip install scrapy==1.0.5 pymongo mongoengine)

VOLUME ["/home/app"]

EXPOSE 8000
EXPOSE 8888

CMD ["bin/bash"]

