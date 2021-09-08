from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

# Печатаем список узлов пример 1
for host in zapi.host.get(output=['hostid', 'host', 'name'], selectInterfaces=['ip', 'port', 'dns']):
    print(host)

# Печатаем список узлов пример 2
host_and_ip = zapi.host.get(output=['hostid', 'host', 'name'], selectInterfaces=['ip', 'port', 'dns'])
for i in host_and_ip:
    # print(i)
    print(i['host'], i['name'], i['interfaces'])

# Завершаем подключения
zapi.user.logout()