FROM index.alauda.cn/ericlung/python

COPY . /opt/
RUN (pip install django)

VOLUME ["/opt/app", "/opt/app"]
EXPOSE 8000
CMD ["python", "/opt/conf/conf.py"]

