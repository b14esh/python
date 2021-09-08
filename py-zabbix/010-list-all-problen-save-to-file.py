from contextlib import redirect_stdout
from datetime import datetime
from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#Zabbix ведет время от создания linux
#Для уточнения времени исполняем стандартную команду linux
#date -d @1620925819
#date +%s

# Получаем все проблемы для группы хостов groupids=2 начиная с даты 1620925819 (Чт 13 мая 2021 20:10:19 MSK)
problem = zapi.event.get(groupids=2,time_from=1620925819)
## Может пригодится для уточнения объектов
##print("\n", problem)

#Запись CSV файла
with open('out.csv', 'w', encoding='utf_8') as f:
    with redirect_stdout(f):
        for pr in problem:
            print("{0};{1};{2} ".format(pr['eventid'], pr['name'], datetime.utcfromtimestamp(int(pr['clock'])).strftime('%Y-%m-%d %H:%M:%S')))


# Завершаем подключения
zapi.user.logout()