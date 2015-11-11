FROM daocloud.io/longminxiang/ubuntu1204

RUN (apt-get --yes --force-yes install python-dev python-pip &&\
cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple"\
>> pip.conf)

