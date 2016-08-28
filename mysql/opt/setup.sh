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

