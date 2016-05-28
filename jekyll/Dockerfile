FROM index.alauda.cn/library/ruby:2.3

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (cd /etc/apt/ &&\
mv sources.list sources_backup.list &&\
echo "\n# aliyun sources\n\n\
deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib\n\
deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib\n\
deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib\n\
deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib\n"\
>> sources.list && apt-get update)

RUN (apt-get --yes install nginx &&\
apt-get clean &&\
apt-get autoclean &&\
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*)

RUN (gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/)

RUN (gem install jekyll)

VOLUME ["/home"]
VOLUME ["/var/www/html"]

EXPOSE 80
EXPOSE 4000

CMD ["nginx", "-g", "daemon off;"]

