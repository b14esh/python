from datetime import datetime
from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)


#Печатаем список групп
print(f" \nПечатаем список групп:")
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
        print (group['groupid'],group['name'])

# Получаем триггеры группы узлов с groupids = 2
triggers = zapi.trigger.get(groupids=2, output='extend', expandDescription=1, selectHosts=['host'],)

#print(f"\n Печатаем все триггеры groupids2 {triggers}")

print("\n")

# Печатаем триггеры
for t in triggers:
    print("{0} - {1} - {2}".format(t['hosts'][0]['host'], t['description'], datetime.utcfromtimestamp(int(t['lastchange'])).strftime('%Y-%m-%d %H:%M:%S')))

# Завершаем подключения
zapi.user.logout()