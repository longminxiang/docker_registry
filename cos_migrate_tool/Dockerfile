FROM java:8

LABEL maintainer="EricLong@longminxiang@163.com"

WORKDIR /cos

COPY migrate_tool.jar /cos

RUN mkdir log tmp

CMD java -jar migrate_tool.jar