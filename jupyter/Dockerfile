FROM python:2.7

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd root &&\
mkdir .pip &&\
cd .pip &&\
echo "\n[global]\n\
index-url = http://pypi.douban.com/simple\n\
--trusted-host = pypi.douban.com"\
>> pip.conf)

RUN (pip install jupyter)

ENTRYPOINT ["jupyter", "notebook"]