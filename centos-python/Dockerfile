FROM centos:7

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (yum update && yum -y install epel-release &&\
yum -y install python-pip python-devel &&\
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

RUN (cd /var && echo -e "#!/bin/sh\nwhile true\ndo\nsleep 10000\ndone" >> daemon.sh)

CMD ["sh", "/var/daemon.sh"]
