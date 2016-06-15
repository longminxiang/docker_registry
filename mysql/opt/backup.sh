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