from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'


# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#Печатаем все группы узлов
print(f" \nПечатаем список групп:")
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
        print (group['groupid'],group['name'])



#Список ид teplate и имя teplate
teplates = zapi.template.get(with_items=1)

# для теста вывалить все в teplates
#print(teplates)

for i in teplates:
    print(i['templateid'], i['host'])

# Создаем узел blablalbalba1 c "ip": "8.8.8.9" в группе с id 5
zapi.do_request(method="host.create",params={
        "host": "blablalbalba3",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "8.8.8.9",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "5"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
    }
)

# Проверяем
print(f" \nПолучаем список хостов в группе с id 5")
hosts = zapi.host.get(groupids=5, output=['hostid','name'])
for host in hosts:
        print (host['hostid'],host['name'])



# Завершаем подключения
zapi.user.logout()