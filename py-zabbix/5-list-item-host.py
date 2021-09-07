from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER '
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#Получаем список item с хоста c id 10268
print(f" \nПолучаем список item с хоста c id 10268")
items = zapi.item.get(hostids=10268, output=['itemid','name'])
for item in items:
        print (item['itemid'],item['name'])

# Завершаем подключения
zapi.user.logout()