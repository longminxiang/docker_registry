# /bin/bash

if [ $MYSQL_OPEN_BACKUP -ne 1 ]; then
    echo "backup not open"
    mkdir /backup/11$MYSQL_OPEN_BACKUP
    exit 0
fi

service cron start

