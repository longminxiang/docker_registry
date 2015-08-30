FROM index.alauda.cn/ericlung/python

COPY . /opt/
RUN (pip install django &&\
pip install -r /opt/app/requirements.txt)

VOLUME ["/opt/app", "/opt/app"]
EXPOSE 80
CMD ["python", "/opt/conf/conf.py"]

