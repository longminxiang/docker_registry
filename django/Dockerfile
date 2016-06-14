FROM centos:7

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (yum -y update &&\
yum -y install epel-release &&\
yum -y install python-pip python-devel MySQL-python gcc libjpeg-turbo-devel libpng-devel &&\
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

RUN (pip install django==1.8.6 uwsgi Pillow django-imagekit)

COPY ./conf /opt/conf

EXPOSE 8000
EXPOSE 8888

CMD ["python", "/opt/conf/conf.py"]

