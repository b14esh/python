from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

# Добываем информацию узлы
# monitored_host - "флаг" - Возврат узлов сети только под наблюдением.
result1 = zapi.host.get(monitored_hosts=1, output='extend')

# Формируем список
hostnames1 = [host['host'] for host in result1]
# Если нужно можем распечатать список
# print(hostnames1)
# Печатаем список хостов красиво
for i in hostnames1:
     print(i)

# Завершаем подключения
zapi.user.logout()