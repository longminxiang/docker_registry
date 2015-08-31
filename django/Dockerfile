FROM index.alauda.cn/ericlung/python

COPY ./conf/conf.py /opt/
RUN (pip install django)

VOLUME ["/home/app"]
EXPOSE 8000
CMD ["python", "/opt/conf.py"]

