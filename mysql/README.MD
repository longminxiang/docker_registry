## 简介

基于官方mysql版本5.7.10

修改：

1. 替换源为阿里源

2. 增加crontab，方便执行定时任务

3. 增加/opt/setup.sh，容器启动时会运行此脚本

4. 增加/opt/backup.sh，备份脚本

## 备份

运行备份脚本

    sh /opt/backup.sh

## 通过crontab自动备份

通过环境变量来控制是否开启自动备份

    MYSQL_OPEN_BACKUP=1

修改setup.sh脚本为

    # /bin/bash

    if [ $MYSQL_OPEN_BACKUP -ne 1 ]; then
        echo "backup not open"
        mkdir /backup/11$MYSQL_OPEN_BACKUP
        exit 0
    fi

    rm /tmp/cron

    #每3个小时备份一次
    echo "0 */3 * * * sh /opt/backup.sh" >> /tmp/cron

    crontab /tmp/cron

    service cron start