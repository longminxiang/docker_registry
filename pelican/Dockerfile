FROM apihackers/pelican

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (apk --update --no-cache add nginx make && mkdir /run/nginx)

RUN (echo -e "#!/bin/sh\n\n\
path=\"/home/pelican/\"\n\n\
if [ -d \"\$path\" ]; then\n\
    cd \"\$path\"\n\
    rm -rf output\n\
    make html\n\n\
    cp -r output/* /var/lib/nginx/html\n\
    rm -rf output\n\
    rm -rf __pycache__\n\
fi\n\n\
nginx -g 'daemon off;'"\
>> /run.sh)

CMD ["sh", "/run.sh"]