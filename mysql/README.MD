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

备份脚本/opt/backup.sh

    # /bin/bash

    # 备份位置
    BDIR=/backup/

    # 需要备份的数据库，可设置多个: mysql db1 db2
    MYSQL_BACKUP_DBS=mysql

    # 数据库密码，Docker环境变量在crontab执行脚本时不起作用，所以在此重新设置
    MYSQL_ROOT_PASSWORD=123456

    # 删除7天前的备份
    OLD_FILES=`date +%Y%m%d -d '-7 days'`*

    cd $BDIR
    rm -rf $OLD_FILES

    DATE=`date +%Y%m%d%H%M`

    echo $MYSQL_BACKUP_DBS

    for DB_NAME in $MYSQL_BACKUP_DBS
    do
        echo 'start backup' $DB_NAME
        FILE_PATH=${BDIR}${DATE}_${DB_NAME}.tar.gz
        mysqldump -u root -p$MYSQL_ROOT_PASSWORD ${DB_NAME} > ${DB_NAME}.sql
        tar -zcvf $FILE_PATH ${DB_NAME}.sql
        rm ${DB_NAME}.sql
        /bin/sleep 3
    done

## 通过crontab自动备份

通过环境变量来控制是否开启自动备份

    MYSQL_OPEN_BACKUP=1

修改setup.sh脚本为

    # /bin/bash

    if [ $MYSQL_OPEN_BACKUP -ne 1 ]; then
        echo "backup not open"
        exit 0
    fi

    rm /tmp/cron

    #每3个小时备份一次
    echo "0 */3 * * * sh /opt/backup.sh" >> /tmp/cron

    crontab /tmp/cron

    service cron start