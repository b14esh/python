###!!!! из доков Для получения проблем, которые были решены ранее, используйте event.get метод.
from datetime import datetime
from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'


# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

## Получаем все проблемы по хосту hsrv1_factoria
## !!! На самом деле не все!!! из доков Для получения проблем, которые были решены ранее, используйте event.get метод.
problem = zapi.problem.get(host='hsrv1_factoria', recent='true')

##print("\n", problem)
for pr in problem:
   #print("{0} - {1} - {2} ".format(pr['eventid'], pr['name'], pr['clock']))
   print("{0} - {1} - {2} ".format(pr['eventid'], pr['name'], datetime.utcfromtimestamp(int(pr['clock'])).strftime('%Y-%m-%d %H:%M:%S')))


# Завершаем подключения
zapi.user.logout()