#!/bin/bash

#Cramos le directorio si no existe
mkdir -p ~/laboratorio/logs/

LOG=~/laboratorio/logs/script.log
log (){
	echo "$(date "+%Y-%m-%d %H:%M:%S") -$1 " >> $LOG
}

for servicio in ssh cron ufw fail2ban; do
    status=$(systemctl is-active $servicio 2>/dev/null)
        log " El $servicio está $status"
done
