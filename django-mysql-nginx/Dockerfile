FROM ubuntu:12.04

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# 163 sources\n\n\
deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse"\
>> sources.list &&\
apt-get update)

RUN (apt-get --yes --force-yes install python-dev python-pip mysql-client libmysqlclient-dev python-mysqldb nginx)

RUN (cd /etc/python2.7 &&\
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

RUN (cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple"\
>> pip.conf)

RUN (pip install uwsgi && pip install django)

CMD ["nginx", "-g", "daemon off;"]
