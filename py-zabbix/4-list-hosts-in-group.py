from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'


# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)


print(f" \nПечатаем список групп:")
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
        print (group['groupid'],group['name'])

print(f" \nПолучаем список хостов в группе с id 2")
hosts = zapi.host.get(groupids=2, output=['hostid','name'])
for host in hosts:
        print (host['hostid'],host['name'])

# Завершаем подключения
zapi.user.logout()