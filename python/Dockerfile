FROM index.alauda.cn/ericlung/ubuntu

RUN (apt-get install python2.7 python-dev python-pip &&\
cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple"\
>> pip.conf)

