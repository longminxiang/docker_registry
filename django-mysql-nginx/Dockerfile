FROM index.alauda.cn/ericlung/django-mysql

RUN (apt-get update && apt-get --yes --force-yes install nginx)
RUN (pip install uwsgi)

CMD ["nginx", "-g", "daemon off;"]
