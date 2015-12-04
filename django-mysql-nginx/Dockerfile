FROM ubuntu:12.04

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/ubuntu/ precise main restricted\n\
deb-src http://mirrors.163.com/ubuntu/ precise main restricted\n\
deb http://mirrors.163.com/ubuntu/ precise-updates main restricted\n\
deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted\n\
deb http://mirrors.163.com/ubuntu/ precise universe\n\
deb-src http://mirrors.163.com/ubuntu/ precise universe\n\
deb http://mirrors.163.com/ubuntu/ precise-updates universe\n\
deb-src http://mirrors.163.com/ubuntu/ precise-updates universe\n\
deb http://mirrors.163.com/ubuntu/ precise multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ precise multiverse\n\
deb http://mirrors.163.com/ubuntu/ precise-updates multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ precise-updates multiverse\n\
deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ precise-security main restricted\n\
deb-src http://mirrors.163.com/ubuntu/ precise-security main restricted\n\
deb http://mirrors.163.com/ubuntu/ precise-security universe\n\
deb-src http://mirrors.163.com/ubuntu/ precise-security universe\n\
deb http://mirrors.163.com/ubuntu/ precise-security multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ precise-security multiverse\n\
deb http://extras.ubuntu.com/ubuntu precise main\n\
deb-src http://extras.ubuntu.com/ubuntu precise main"\
>> sources.list &&\
apt-get update &&\
apt-get --yes --force-yes install python-dev python-pip \
mysql-client libmysqlclient-dev python-mysqldb &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple"\
>> pip.conf &&\
cd /etc/python2.7 &&\
mv sitecustomize.py sitecustomize_backup &&\
echo "import sys\n\
reload(sys)\n\
sys.setdefaultencoding('utf-8')\n\
try:\n\
    import apport_python_hook\n\
except ImportError:\n\
    pass\n\
else:\n\
    apport_python_hook.install()"\
>> sitecustomize.py)

RUN (pip install django==1.8.6 && pip install uwsgi)

CMD ["nginx", "-g", "daemon off;"]
